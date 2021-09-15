import os
import sys
from classes.database import Database
import json
from dotenv import load_dotenv
import logging


class Footnote(object):
    def __init__(self):
        logging.basicConfig(filename='log/app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
        self.code = ""
        self.content = ""

    def save(self):
        d = Database()
        sql = """
        INSERT INTO roo.footnotes
        (code, content)
        VALUES (%s, %s)
        ON CONFLICT (code) DO UPDATE
        SET content = %s
        """
        # UPDATE SET content = %s
        
        params = [
            self.code,
            self.content,
            self.content,
        ]
        d.run_query(sql, params)
