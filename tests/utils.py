import requests
import allure
import curlify
import logging


def log_post_request(url, **kwargs):
    with allure.step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=allure.attachment_type.TEXT, extension="txt")
        logging.info(curlify.to_curl(response.request))
        return response
