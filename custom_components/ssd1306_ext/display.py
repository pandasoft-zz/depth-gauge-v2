import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import ssd1306_base, i2c
from esphome.const import CONF_ID, CONF_LAMBDA, CONF_PAGES

AUTO_LOAD = ['ssd1306_base']
DEPENDENCIES = ['i2c']

ssd1306_ext = cg.esphome_ns.namespace('ssd1306_ext')
EXTSSD1306 = ssd1306_ext.class_('EXTSSD1306', ssd1306_base.SSD1306, i2c.I2CDevice)

CONFIG_SCHEMA = cv.All(ssd1306_base.SSD1306_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(EXTSSD1306),
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x3C)),
                       cv.has_at_most_one_key(CONF_PAGES, CONF_LAMBDA))


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield ssd1306_base.setup_ssd1036(var, config)
    yield i2c.register_i2c_device(var, config)
