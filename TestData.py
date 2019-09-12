import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Lesson4prj.settings')

import django
django.setup()

#Faker
import random
from faker import Faker
from less4App.models import Employee

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakegen.first_name()
        fake_dob= fakegen.date()
        fake_email= fakegen.email()
        fake_salary= fakegen.random_int()

        st = Employee.objects.get_or_create(name=fake_name,dob= fake_dob,email=fake_email,salary=fake_salary)[0]
        st.save()
    return st

if __name__ == "__main__" :
    print('Populate Records')
    populate(20)
    print('Populate complete')

"""
id = str(uuid.uuid4())
        full_name = fake.name()
        gender = random.choice(['Male','Female'])
        date_of_birth = random_date
        education_level = random.choice(['None', 'Elementary (<6th Grade', 'Highschool (7th - 10th Grade)','Preparatory(10-12th Grade)', 'University/College', 'Bachelor(BA/Bsc)','Masters(MA/Msc)','PhD/MD'])

        work_experience = random.uniform(0.0,40.0)
        job_title=fake.job()
        job_description=fake.sentence()
        post_date = datetime.now()

        dir(fakegen)
date_between', 'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century', 'date_this_decade',
'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates',
'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year',
'day_of_month', 'day_of_week', 'domain_name', 'domain_word', 'ean', 'ean13', 'ean8', 'ein', 'email',
'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male',
'format', 'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'get_formatter', 'get_providers',
'hex_color', 'hexify', 'hostname', 'iban', 'image_url', 'internet_explorer', 'ipv4', 'ipv4_network_class',
'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'itin', 'job', 'language_code',
'last_name', 'last_name_female', 'last_name_male', 'latitude', 'latlng', 'lexify', 'license_plate',
'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 'location_on_land', 'longitude',
'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 'military_dpo', 'military_ship',
'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male',
'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date',
'past_datetime', 'phone_number', 'postalcode', 'postalcode_in_state', 'postalcode_plus4', 'postcode',
'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male', 'profile', 'provider', 'providers', 'pybool',
'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystruct', 'pytuple',
'random', 'random_choices', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty',
'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter',
'random_letters', 'random_lowercase_letter', 'random_number', 'random_sample',
'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color',
'safari', 'safe_color_name', 'safe_email', 'safe_hex_color', 'secondary_address', 'seed', 'seed_instance',
'sentence', 'sentences', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state',
'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female',
'suffix_male', 'text', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'unix_device',
'unix_partition', 'unix_time', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent',
 'user_name', 'uuid4', 'windows_platform_token', 'word', 'words', 'year', 'zipcode', 'zipcode_in_state', 'zipcode_plus4']
>>>

"""
