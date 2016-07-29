import requests

class CrlCpLib:

    def __init__(self, username=None, password=None):
        self.status_code = None
        self.status_text = None
        self.user = username
        self.password = password

    def check_credentials(self, base_url):
        r = requests.get(base_url, auth=(self.user, self.password))
        self._set_status_vars(r.status_code, r.reason)
        self.status_code_should_be(200)
        return self.status_code

    def open_file(self, filename):
        r = requests.get(filename, auth=(self.user, self.password))
        self._set_status_vars(r.status_code, r.reason)
        return self.status_code

    def copy_file_to(self, filename, destination):
        with open(filename, 'rb') as data:
            r = requests.put(destination, data=data, auth=(self.user, self.password))
        self._set_status_vars(r.status_code, r.reason)
        return self.status_code

    def delete_file(self, filename):
        r = requests.delete(filename, auth=(self.user, self.password))
        self._set_status_vars(r.status_code, r.reason)
        return self.status_code

    def download_file_as(self, file_to_download, local_filename):
        r = requests.get(file_to_download, stream=True, auth=(self.user, self.password))
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        self._set_status_vars(r.status_code, r.reason)
        return self.status_code

    def status_code_should_be(self, expected_status_code):
        if not int(expected_status_code) == self.status_code:
            raise AssertionError("Expected status code: " + str(expected_status_code) + " but got: " + str(self.status_code))

    def status_text_should_be(self, expected_status_text):
        if not expected_status_text == self.status_text:
            raise AssertionError("Expected status text: " + expected_status_text + " but got: " + self.status_text)

    def _set_status_vars(self, status_code, status_text):
        self.status_code = status_code
        self.status_text = status_text