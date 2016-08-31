from configparser import ConfigParser

def try_types(config, section, inner_key):
    try:
        return config.getint(section, inner_key)
    except ValueError:
        try:
            return config.getboolean(section, inner_key)
        except ValueError:

            return config.get(section, inner_key)



class SettingsLoadStrategyConf(object):
    """
    This is the strategy used to read settings from conf files or ini files
    Note that the section name and item anme are capatilsed and concatenated
    thus
    [default]
    host=localhost
    
    becomes
    DEFAULT_HOST='localhost'
    """
    name = 'conf'

    @staticmethod
    def is_valid_file(file_name):
        return file_name.endswith('.conf')

    @classmethod
    def load_settings_file(cls, settings_file):
        result = {}
        config = ConfigParser()
        config.read(constants.CONFIG_SETTINGS)
        d = dict(config._sections)
        for section, outer_dict in d.items():
            for inner_key, inner_item in outer_dict.items():
                value_to_set = try_types(config, section, inner_key)
                key_to_set = "%s_%s" % (section.upper(), inner_key.upper())
                result[key_to_set] = value_to_set
        return result


