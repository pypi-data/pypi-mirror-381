from __future__ import annotations

import math
import random
import time
from datetime import datetime, date
from typing import Optional
from urllib.parse import urlparse, urlunparse, unquote

import regex as re
from bs4 import BeautifulSoup
from bs4.element import Tag

from jobspy_enhanced.exception import LinkedInException
from jobspy_enhanced.linkedin.constant import headers
from jobspy_enhanced.linkedin.util import (
    is_job_remote,
    job_type_code,
    parse_job_type,
    parse_job_level,
    parse_company_industry
)
from jobspy_enhanced.model import (
    JobPost,
    Location,
    JobResponse,
    Country,
    Compensation,
    DescriptionFormat,
    Scraper,
    ScraperInput,
    Site,
)
from jobspy_enhanced.util import (
    extract_emails_from_text,
    currency_parser,
    markdown_converter,
    plain_converter,
    create_session,
    remove_attributes,
    create_logger,
)

log = create_logger("LinkedIn")


class LinkedIn(Scraper):
    base_url = "https://www.linkedin.com"
    delay = 3
    band_delay = 4
    jobs_per_page = 25

    def __init__(
        self, proxies: list[str] | str | None = None, ca_cert: str | None = None, user_agent: str | None = None
    ):
        """
        Initializes LinkedInScraper with the LinkedIn job search url
        """
        super().__init__(Site.LINKEDIN, proxies=proxies, ca_cert=ca_cert)
        self.session = create_session(
            proxies=self.proxies,
            ca_cert=ca_cert,
            is_tls=False,
            has_retry=True,
            delay=5,
            clear_cookies=True,
        )
        self.session.headers.update(headers)
        self.scraper_input = None
        self.country = "worldwide"
        self.job_url_direct_regex = re.compile(r'(?<=\?url=)[^"]+')

    def scrape(self, scraper_input: ScraperInput) -> JobResponse:
        """
        Scrapes LinkedIn for jobs with scraper_input criteria
        :param scraper_input:
        :return: job_response
        """
        self.scraper_input = scraper_input
        job_list: list[JobPost] = []
        seen_ids = set()
        start = scraper_input.offset // 10 * 10 if scraper_input.offset else 0
        request_count = 0
        seconds_old = (
            scraper_input.hours_old * 3600 if scraper_input.hours_old else None
        )
        continue_search = (
            lambda: len(job_list) < scraper_input.results_wanted and start < 1000
        )
        while continue_search():
            request_count += 1
            log.info(
                f"search page: {request_count} / {math.ceil(scraper_input.results_wanted / 10)}"
            )
            params = {
                "keywords": scraper_input.search_term,
                "location": scraper_input.location,
                "distance": scraper_input.distance,
                "pageNum": 0,
                "start": start,
            }
            
            # Add all applicable filters (no longer mutually exclusive)
            if scraper_input.is_remote:
                params["f_WT"] = 2
                
            if scraper_input.job_type:
                params["f_JT"] = job_type_code(scraper_input.job_type)
                
            if scraper_input.easy_apply:
                params["f_AL"] = "true"
                
            if scraper_input.linkedin_company_ids:
                params["f_C"] = ",".join(map(str, scraper_input.linkedin_company_ids))
                
            # Add time filter if specified (can now be combined with other filters)
            if seconds_old is not None:
                params["f_TPR"] = f"r{seconds_old}"

            params = {k: v for k, v in params.items() if v is not None}
            try:
                response = self.session.get(
                    f"{self.base_url}/jobs-guest/jobs/api/seeMoreJobPostings/search?",
                    params=params,
                    timeout=10,
                )
                if response.status_code not in range(200, 400):
                    if response.status_code == 429:
                        err = (
                            f"429 Response - Blocked by LinkedIn for too many requests"
                        )
                    else:
                        err = f"LinkedIn response status code {response.status_code}"
                        err += f" - {response.text}"
                    log.error(err)
                    return JobResponse(jobs=job_list)
            except Exception as e:
                if "Proxy responded with" in str(e):
                    log.error(f"LinkedIn: Bad proxy")
                else:
                    log.error(f"LinkedIn: {str(e)}")
                return JobResponse(jobs=job_list)

            soup = BeautifulSoup(response.text, "html.parser")
            job_cards = soup.find_all("div", class_="base-search-card")
            if len(job_cards) == 0:
                return JobResponse(jobs=job_list)

            for job_card in job_cards:
                href_tag = job_card.find("a", class_="base-card__full-link")
                if href_tag and "href" in href_tag.attrs:
                    href = href_tag.attrs["href"].split("?")[0]
                    job_id = href.split("-")[-1]

                    if job_id in seen_ids:
                        continue
                    seen_ids.add(job_id)

                    try:
                        fetch_desc = scraper_input.linkedin_fetch_description
                        job_post = self._process_job(job_card, job_id, fetch_desc)
                        if job_post:
                            job_list.append(job_post)
                        if not continue_search():
                            break
                    except Exception as e:
                        raise LinkedInException(str(e))

            if continue_search():
                time.sleep(random.uniform(self.delay, self.delay + self.band_delay))
                start += len(job_cards)

        job_list = job_list[: scraper_input.results_wanted]
        return JobResponse(jobs=job_list)

    def _process_job(
        self, job_card: Tag, job_id: str, full_descr: bool
    ) -> Optional[JobPost]:
        salary_tag = job_card.find("span", class_="job-search-card__salary-info")

        compensation = description = None
        if salary_tag:
            salary_text = salary_tag.get_text(separator=" ").strip()
            salary_values = [currency_parser(value) for value in salary_text.split("-")]
            salary_min = salary_values[0]
            salary_max = salary_values[1]
            currency = salary_text[0] if salary_text[0] != "$" else "USD"

            compensation = Compensation(
                min_amount=int(salary_min),
                max_amount=int(salary_max),
                currency=currency,
            )

        title_tag = job_card.find("span", class_="sr-only")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        company_tag = job_card.find("h4", class_="base-search-card__subtitle")
        company_a_tag = company_tag.find("a") if company_tag else None
        company_url = (
            urlunparse(urlparse(company_a_tag.get("href"))._replace(query=""))
            if company_a_tag and company_a_tag.has_attr("href")
            else ""
        )
        company = company_a_tag.get_text(strip=True) if company_a_tag else "N/A"

        metadata_card = job_card.find("div", class_="base-search-card__metadata")
        location = self._get_location(metadata_card)

        # Try multiple selectors for date posted information
        date_posted = None
        
        if metadata_card:
            # Try different possible selectors for date information
            datetime_tag = None
            
            # First try: job-search-card__listdate class
            datetime_tag = metadata_card.find("time", class_="job-search-card__listdate")
            
            # Second try: any time tag with datetime attribute
            if not datetime_tag:
                datetime_tag = metadata_card.find("time", attrs={"datetime": True})
            
            # Third try: look for relative time text and parse it
            if not datetime_tag:
                time_elements = metadata_card.find_all("time")
                for time_elem in time_elements:
                    if time_elem.get("datetime"):
                        datetime_tag = time_elem
                        break
            
            # Fourth try: look for any element with datetime attribute
            if not datetime_tag:
                datetime_tag = metadata_card.find(attrs={"datetime": True})
            
            # Parse the datetime if found
            if datetime_tag and "datetime" in datetime_tag.attrs:
                datetime_str = datetime_tag["datetime"]
                try:
                    # Try different datetime formats
                    for fmt in ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%SZ"]:
                        try:
                            date_posted = datetime.strptime(datetime_str, fmt).date()
                            break
                        except ValueError:
                            continue
                except:
                    date_posted = None
            
            # If still no date found, try to parse relative time text
            if not date_posted:
                date_posted = self._parse_relative_date(metadata_card)
        job_details = {}
        if full_descr:
            job_details = self._get_job_details(job_id)
            description = job_details.get("description")
        is_remote = is_job_remote(title, description, location)

        return JobPost(
            id=f"li-{job_id}",
            title=title,
            company_name=company,
            company_url=company_url,
            location=location,
            is_remote=is_remote,
            date_posted=date_posted,
            job_url=f"{self.base_url}/jobs/view/{job_id}",
            compensation=compensation,
            job_type=job_details.get("job_type"),
            job_level=job_details.get("job_level", "").lower(),
            company_industry=job_details.get("company_industry"),
            description=job_details.get("description"),
            job_url_direct=job_details.get("job_url_direct"),
            emails=extract_emails_from_text(description),
            company_logo=job_details.get("company_logo"),
            job_function=job_details.get("job_function"),
        )

    def _get_job_details(self, job_id: str) -> dict:
        """
        Retrieves job description and other job details by going to the job page url
        :param job_page_url:
        :return: dict
        """
        try:
            response = self.session.get(
                f"{self.base_url}/jobs/view/{job_id}", timeout=5
            )
            response.raise_for_status()
        except:
            return {}
        if "linkedin.com/signup" in response.url:
            return {}

        soup = BeautifulSoup(response.text, "html.parser")
        div_content = soup.find(
            "div", class_=lambda x: x and "show-more-less-html__markup" in x
        )
        description = None
        if div_content is not None:
            div_content = remove_attributes(div_content)
            description = div_content.prettify(formatter="html")
            if self.scraper_input.description_format == DescriptionFormat.MARKDOWN:
                description = markdown_converter(description)
            elif self.scraper_input.description_format == DescriptionFormat.PLAIN:
                description = plain_converter(description)
        h3_tag = soup.find(
            "h3", text=lambda text: text and "Job function" in text.strip()
        )

        job_function = None
        if h3_tag:
            job_function_span = h3_tag.find_next(
                "span", class_="description__job-criteria-text"
            )
            if job_function_span:
                job_function = job_function_span.text.strip()

        company_logo = (
            logo_image.get("data-delayed-url")
            if (logo_image := soup.find("img", {"class": "artdeco-entity-image"}))
            else None
        )
        return {
            "description": description,
            "job_level": parse_job_level(soup),
            "company_industry": parse_company_industry(soup),
            "job_type": parse_job_type(soup),
            "job_url_direct": self._parse_job_url_direct(soup),
            "company_logo": company_logo,
            "job_function": job_function,
        }

    def _get_location(self, metadata_card: Optional[Tag]) -> Location:
        """
        Extracts the location data from the job metadata card.
        :param metadata_card
        :return: location
        """
        location = Location(country=Country.from_string(self.country))
        if metadata_card is not None:
            location_tag = metadata_card.find(
                "span", class_="job-search-card__location"
            )
            location_string = location_tag.text.strip() if location_tag else "N/A"
            parts = location_string.split(", ")
            if len(parts) == 2:
                city, state = parts
                location = Location(
                    city=city,
                    state=state,
                    country=Country.from_string(self.country),
                )
            elif len(parts) == 3:
                city, state, country = parts
                country = Country.from_string(country)
                location = Location(city=city, state=state, country=country)
        return location

    def _parse_job_url_direct(self, soup: BeautifulSoup) -> str | None:
        """
        Gets the job url direct from job page
        :param soup:
        :return: str
        """
        job_url_direct = None
        job_url_direct_content = soup.find("code", id="applyUrl")
        if job_url_direct_content:
            job_url_direct_match = self.job_url_direct_regex.search(
                job_url_direct_content.decode_contents().strip()
            )
            if job_url_direct_match:
                job_url_direct = unquote(job_url_direct_match.group())

        return job_url_direct

    def _parse_relative_date(self, metadata_card) -> Optional[date]:
        """
        Parse relative date strings like "2 days ago", "1 week ago", etc.
        :param metadata_card: BeautifulSoup element containing metadata
        :return: date object or None
        """
        if not metadata_card:
            return None
            
        # Look for text that might contain relative dates
        text_content = metadata_card.get_text().lower()
        
        # Common relative date patterns
        import re
        from datetime import timedelta
        
        today = datetime.now().date()
        
        # Pattern for "X days ago"
        days_match = re.search(r'(\d+)\s+days?\s+ago', text_content)
        if days_match:
            days = int(days_match.group(1))
            return today - timedelta(days=days)
        
        # Pattern for "X weeks ago"
        weeks_match = re.search(r'(\d+)\s+weeks?\s+ago', text_content)
        if weeks_match:
            weeks = int(weeks_match.group(1))
            return today - timedelta(weeks=weeks)
        
        # Pattern for "X months ago"
        months_match = re.search(r'(\d+)\s+months?\s+ago', text_content)
        if months_match:
            months = int(months_match.group(1))
            # Approximate months as 30 days
            return today - timedelta(days=months * 30)
        
        # Pattern for "X years ago"
        years_match = re.search(r'(\d+)\s+years?\s+ago', text_content)
        if years_match:
            years = int(years_match.group(1))
            # Approximate years as 365 days
            return today - timedelta(days=years * 365)
        
        # Pattern for "yesterday"
        if 'yesterday' in text_content:
            return today - timedelta(days=1)
        
        # Pattern for "today"
        if 'today' in text_content:
            return today
        
        # Look for any time element that might have relative text
        time_elements = metadata_card.find_all("time")
        for time_elem in time_elements:
            time_text = time_elem.get_text().lower()
            if any(keyword in time_text for keyword in ['ago', 'yesterday', 'today']):
                # Try to parse this specific time element
                return self._parse_relative_date_from_text(time_text)
        
        return None
    
    def _parse_relative_date_from_text(self, text: str) -> Optional[date]:
        """
        Parse relative date from a specific text string
        :param text: text containing relative date
        :return: date object or None
        """
        import re
        from datetime import timedelta
        
        today = datetime.now().date()
        text = text.lower().strip()
        
        # Pattern for "X days ago"
        days_match = re.search(r'(\d+)\s+days?\s+ago', text)
        if days_match:
            days = int(days_match.group(1))
            return today - timedelta(days=days)
        
        # Pattern for "X weeks ago"
        weeks_match = re.search(r'(\d+)\s+weeks?\s+ago', text)
        if weeks_match:
            weeks = int(weeks_match.group(1))
            return today - timedelta(weeks=weeks)
        
        # Pattern for "X months ago"
        months_match = re.search(r'(\d+)\s+months?\s+ago', text)
        if months_match:
            months = int(months_match.group(1))
            return today - timedelta(days=months * 30)
        
        # Pattern for "X years ago"
        years_match = re.search(r'(\d+)\s+years?\s+ago', text)
        if years_match:
            years = int(years_match.group(1))
            return today - timedelta(days=years * 365)
        
        # Pattern for "yesterday"
        if 'yesterday' in text:
            return today - timedelta(days=1)
        
        # Pattern for "today"
        if 'today' in text:
            return today
        
        return None
