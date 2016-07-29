from auth_vars import USERNAME, PASSWORD
from CrlCpLib import CrlCpLib


prometheus_url = "https://prometheus.desy.de/Users/" + USERNAME + "/Private/"

curl_boy = CrlCpLib(prometheus_url, USERNAME, PASSWORD)

curl_boy.check_credentials()

# File copy test

curl_boy.copy_file_to("/home/andy/CMSCalorimeter.png", "CMSCalorimeter.png")
curl_boy.status_code_should_be(201)

# File delete test

curl_boy.delete_file("CMSCalorimeter.png")
curl_boy.status_code_should_be(204)

# File download test

curl_boy.download_file_as("testfile", "/home/andy/testfile")
curl_boy.status_code_should_be(200)