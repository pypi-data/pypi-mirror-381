from bs4 import BeautifulSoup, NavigableString, Comment
import random
import datetime
from .settings import load_config


class FreakyFunkyFontsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.config = load_config()

    def __call__(self, request):
        response = self.get_response(request)
        return self.process_response(request, response)

    def process_response(self, request, response):
        if not self.should_apply_to_path(request.path):
            return response
        if not self.should_apply_middleware():
            return response
        if not self.is_html_response(response):
            return response
        soup = self.get_soup(response)
        self.inject_tags(soup)
        self.process_html(soup)
        response.content = soup.encode(formatter="minimal")
        response["Content-Length"] = len(response.content)
        return response

    def should_apply_to_path(self, path):
        import re
        paths = self.config.get("paths", {})
        excludes = paths.get("exclude", []) if paths else []
        includes = paths.get("include", []) if paths else []
        # Exclude logic
        for pattern in excludes:
            if re.match(pattern, path):
                return False
        # Include logic
        if includes:
            return any(re.match(pattern, path) for pattern in includes)
        return True

    def should_apply_middleware(self):
        """Handle date and time range logic"""
        today = datetime.date.today()
        now = datetime.datetime.now().time()
        date_ranges = self.config.get("date_ranges", {})

        def in_date_range(rng):
            # Support both YYYY-MM-DD:YYYY-MM-DD and MM-DD:MM-DD
            start, end = rng.split(":")
            if len(start) == 10 and len(end) == 10:
                # Full date format
                start_date = datetime.date.fromisoformat(start)
                end_date = datetime.date.fromisoformat(end)
                if start_date <= end_date:
                    return start_date <= today <= end_date
                else:
                    return today >= start_date or today <= end_date
            elif len(start) == 5 and len(end) == 5:
                # Month-day format, year-agnostic
                start_md = tuple(map(int, start.split("-")))
                end_md = tuple(map(int, end.split("-")))
                today_md = (today.month, today.day)
                if start_md <= end_md:
                    return start_md <= today_md <= end_md
                else:
                    return today_md >= start_md or today_md <= end_md
            else:
                return False

        def in_time_range(rng):
            start, end = rng.split("-")
            start = datetime.time(*map(int, start.split(":")))
            end = datetime.time(*map(int, end.split(":")))
            if start <= end:
                return start <= now <= end
            else:
                return now >= start or now <= end
        # Exclude logic for date+temporal ranges
        for item in date_ranges.get("exclude", []):
            drange = item["range"]
            if in_date_range(drange):
                temporal = item.get("temporal", [])
                if not temporal or any(in_time_range(tr) for tr in temporal):
                    return False
        # Include logic for date+temporal ranges
        includes = date_ranges.get("include", [])
        if includes and not any(in_date_range(item["range"]) and (not item.get("temporal") or any(in_time_range(tr) for tr in item["temporal"])) for item in includes):
            return False
        return True

    def is_html_response(self, response):
        """Checks if the response is HTML"""
        content_type = response.get("Content-Type", "")
        return "text/html" in content_type

    def get_soup(self, response):
        """Parses the response content"""
        original_content = response.content.decode(response.charset or 'utf-8')
        return BeautifulSoup(original_content, "html.parser")

    def inject_tags(self, soup):
        """Injects extra tags into <head>"""
        inject_tags = self.config["inject"].get("tags", [])
        if soup.head and inject_tags:
            for tag_html in inject_tags:
                if tag_html not in str(soup.head):
                    tag_soup = BeautifulSoup(tag_html, "html.parser")
                    for tag in tag_soup:
                        soup.head.append(tag)

    def process_html(self, soup):
        """Handles scope and root selection"""
        skip_tags = set(self.config["behaviour"]["skip_tags"])
        fonts = self.config["fonts"]["pool"]
        scopes = self.config["behaviour"].get("scopes", ["all"])
        roots = []
        if "all" in scopes:
            roots = [soup.body] if soup.body else [soup]
        else:
            for scope in scopes:
                if scope == "body" and soup.body:
                    roots.append(soup.body)
                else:
                    roots.extend(soup.find_all(scope))
        for root in roots:
            self.process_element(root, skip_tags, fonts, soup)

    def process_element(self, element, skip_tags, fonts, soup):
        """Recursively processes and decorates text nodes with mighty <span> tags with some fonts"""
        if hasattr(element, 'name') and element.name in skip_tags:
            return
        children = list(element.children) if hasattr(element, 'children') else []
        for child in children:
            if isinstance(child, NavigableString) and not isinstance(child, Comment):
                text = str(child)
                if text.strip():
                    new_elements = []
                    for c in text:
                        if c.strip():
                            font = random.choice(fonts)
                            span = soup.new_tag("span")
                            span['style'] = f"font-family:{font}"
                            span.string = c
                            new_elements.append(span)
                        else:
                            new_elements.append(NavigableString(c))
                    for new_el in reversed(new_elements):
                        child.insert_after(new_el)
                    child.extract()
            elif hasattr(child, 'name'):
                self.process_element(child, skip_tags, fonts, soup)