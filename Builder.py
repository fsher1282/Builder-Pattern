

class Builder:

    def __init__(self, f_name, l_name, h_number, street, city, post_code, country):
        self.f_name = f_name
        self.l_name = l_name
        self.h_number = h_number
        self.street = street
        self.city = city
        self.post_code = post_code
        self.country = country
        self.state = ''

    def american_address(self, state):
        self.state = state
        usa_address = '{self.f_name} {self.l_name} \n' \
                      '{self.h_number} {self.street} \n' \
                      '{self.city}, {self.state} {self.post_code} \n' \
                      '{self.country}'.format(self=self)
        return usa_address

    def french_address(self):
        fren_address = '{self.f_name} {self.l_name} \n' \
                       '{self.h_number}, {self.street} \n' \
                       '{self.post_code} {self.city} \n' \
                       '{self.country}'.format(self=self)
        return fren_address

    def hungarian_address(self):
        hung_address = '{self.l_name} {self.f_name} \n' \
                       '{self.post_code}, {self.city} \n' \
                       '{self.h_number} {self.street} \n' \
                       '{self.country}'.format(self=self)

        return hung_address

    def mexican_address(self, state):
        self.state = state
        mexico_address = '{self.f_name} {self.l_name} \n' \
                         '{self.street}, {self.h_number} \n' \
                         '{self.city}, {self.state} \n' \
                         '{self.post_code}'.format(self=self)

        return mexico_address