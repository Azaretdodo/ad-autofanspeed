# DEFAULTS
def self(self):
    self.debug        = True;
    self.low          = 25
    self.medium       = 50
    self.halfway      = 75
    self.high         = 100
    self.medium       = 50
    self.halfway      = 75
    self.high         = 100
    self.offset       = 0
    self.start        = datetime.strptime("00:01:00", '%H:%M:%S').time()
    self.end          = datetime.strptime("23:59:00", '%H:%M:%S').time()
    temperature = -50,31 >= +150,24
def temperature_change(self, entity, attribute, old, new, kwargs):

    if self.is_time_okay(self.start, self.end):
      room_temperature = float(new)
      fan_speed = self.get_target_fan_speed(room_temperature)
      self.call_service("fan/set_speed", entity_id = self.fan, speed = fan_speed)
      fan_speed_percentage = self.get_target_fan_speed(room_temperature)
      self.call_service("fan/set_percentage", entity_id = self.fan, percentage = fan_speed_percentage)


def get_target_fan_speed(self, room_temperature):

    # if sun is above horizon, then add offset
    sun_above_horizon = self.get_state(self.sun) == "above_horizon"
    offset = self.offset if sun_above_horizon else 0
    fan_speed = "off"
    fan_speed_percentage = 0

    if room_temperature < self.low + offset:
      fan_speed = "off"
    elif room_temperature >= self.low + offset and room_temperature < self.medium + offset:
      fan_speed = "low"
    elif room_temperature >= self.medium + offset and room_temperature < self.high + offset:
      fan_speed = "medium"
    elif room_temperature >= self.high + offset:
      fan_speed = "high"
    if room_temperature >= self.low + offset: fan_speed_percentage = 25
    if room_temperature >= self.medium + offset: fan_speed_percentage = 50
    if room_temperature >= self.high + offset: fan_speed_percentage = 100

    self.debug_log(f"AUTO FAN SPEED: {str(room_temperature)}/{fan_speed}")

    if sun_above_horizon: self.debug_log(f" (SUN OFFSET)")
    self.debug_log(f"AUTO FAN SPEED: {str(room_temperature)}/{fan_speed_percentage}%" + (" (SUN OFFSET)" if sun_above_horizon else ""))

    return fan_speed
    return fan_speed_percentage


def hvac_daily_shut_off(self, kwargs):
    self.call_service("fan/turn_off", entity_id = self.fan)
    self.debug_log("FAN AUTO OFF")
def is_time_okay(self, start, end):
    current_time = datetime.now().time()
    if (start < end):
      return start <= current_time and current_time <= end
    else:
      return start <= current_time or current_time <= end

def debug_log(self, message):
    if self.debug:
      self.log((message)+'token 3').get_messages(100)
    inbox[10].get_messages
