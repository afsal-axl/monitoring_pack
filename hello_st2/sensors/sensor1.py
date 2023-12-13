# Copyright 2020 The StackStorm Authors.
# Copyright 2019 Extreme Networks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import eventlet
from st2reactor.sensor.base import Sensor
import requests
import base64



class HelloSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(HelloSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False
        self._file_path = 'https://api.github.com/repos/afsalbadarudeen/Stackstorm/contents/README.md'
        self._previous_content = self.read_file_content()  # Initialize _previous_content here
    def setup(self):
        pass
    def run(self):
        while not self._stop:
            current_content = self.read_file_content()
            if current_content:

                if current_content != self._previous_content:
                    self._logger.debug("HelloSensor dispatching trigger...")
                    count = self.sensor_service.get_value("hello_st2.count") or 0
                    payload = {
                        "greeting": "Stackstorm",
                        "count": int(count) + 1,
                        "content_before": self._previous_content,
                        "content_after": current_content,
                    }
                    self.sensor_service.dispatch(trigger="hello_st2.event1", payload=payload)
                    self.sensor_service.set_value("hello_st2.count", payload["count"])
                
                    self._previous_content = current_content
            
            else:
                self._logger.debug("HelloSensor dispatching trigger...")
                payload = {"error_message": "Error: Unable to fetch file. No internet connection"}
                self.sensor_service.dispatch(trigger="hello_st2.event2", payload=payload)
                


            eventlet.sleep(60)

    def read_file_content(self):
        decoded_content = None
        try:
            response = requests.get(self._file_path)
            content = response.json().get('content', '')
            decoded_content = base64.b64decode(content).decode('utf-8')
        except requests.exceptions.RequestException as e:
            pass
        return decoded_content
    
    def cleanup(self):
        self._stop = True
    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass
    def update_trigger(self, trigger):
        pass
    def remove_trigger(self, trigger):
        pass