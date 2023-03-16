import gateway as gateway
import logging
import time
from datetime import datetime

test_payload_str_normal_1 = "29, 0, 0, 1"
test_payload_str_normal_2 = "29, 0, 0, 1"
test_payload_str_normal_3 = "29, 0, 0, 1"
test_payload_str_normal_3 = "29, 0, 0, 1"

# a dictionary of the topics
GATEWAY = {
    "root": "is215g11t04",
    "full_reading": "is215g11t04/full_reading",
    "alert": "is215g11t04/alert"
}


# Configure logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# initlize the last motion time for people presence monitoring
last_motion_time = time.time()

parameter_name_list = ["temperature",
                       "gas_status", "smoke_status", "motion_reading"]

print(str(gateway.annotate_payload(test_payload_str_normal_1, parameter_name_list)))
print(str(gateway.alert_filter()))
