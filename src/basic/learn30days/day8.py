
class Animal(object):
    name = 'Amy'
    noise = 'Grunt'
    size = 'Large'
    color = 'Brown'
    hair = 'wave'

    def get_color(self):
        return self.color

    @property
    def make_noise(self):
        return self.noise
