#pragma once

#include "esphome/core/component.h"
#include "esphome/components/ssd1306_base/ssd1306_base.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace ssd1306_ext {

class EXTSSD1306 : public ssd1306_base::SSD1306, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void turnOn();
  void turnOff();

 protected:
  void command(uint8_t value) override;
  void write_display_data() override;

  enum ErrorCode { NONE = 0, COMMUNICATION_FAILED } error_code_{NONE};
};

}  // namespace ssd1306_ext
}  // namespace esphome
