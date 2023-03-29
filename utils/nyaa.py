import random
import re

import requests
from bs4 import BeautifulSoup

from utils.singleton import Singleton


class Nyaa(metaclass=Singleton):
    def __init__(self):
        self.domaine = "nyaa.si"

    class Comment:
        def __init__(self, nyaa) -> None:
            self.nyaa = nyaa

        def get(self):
            page_number = random.randint(1, 3)
            page = requests.get(
                f"https://{self.nyaa.domaine}/?s=comments&o=desc&p={page_number}"
            )
            soup = BeautifulSoup(page.content, "html.parser")

            hrefs = [link.get("href") for link in soup.find_all("a", class_="comments")]

            id_regex = r"/view/(\d+)#comments"

            ids = []

            for href in hrefs:
                if id_match := re.search(id_regex, href):
                    id_str = id_match[1]
                    ids.append(int(id_str))

            if ids:
                random_id = random.choice(ids)

                page = requests.get(f"https://{self.nyaa.domaine}/view/{random_id}")
                comment_soup = BeautifulSoup(page.content, "html.parser")

                title = comment_soup.find("h3", {"class": "panel-title"})
                title = title.text.strip()

                if comment_panels := comment_soup.find_all(
                    "div", class_="comment-panel"
                ):
                    return self._extracted_from_get_nyaa_comment(
                        title, comment_panels, random_id
                    )

        @staticmethod
        def _extracted_from_get_nyaa_comment(title, comment_panels, random_id):
            random_comment_panel = random.choice(comment_panels)

            comment_id = random_comment_panel.get("id")
            user_text = random_comment_panel.find("a", title="User").text

            avatar_src = random_comment_panel.find("img", class_="avatar").get("src")
            comment_text = random_comment_panel.find(
                "div", class_="comment-content"
            ).text

            if (
                title
                and random_id
                and comment_id
                and user_text
                and avatar_src
                and comment_text
            ):
                return {
                    "title": title,
                    "release": random_id,
                    "comment": {"id": comment_id, "text": comment_text},
                    "user": {"username": user_text, "avatar": avatar_src},
                }

            return False

    @property
    def comment(self):
        return self.Comment(self)


nyaa = Nyaa()
