#!/bin/python3

# fid (https://github.com/X3NOOO/fid)
# Copyright (C) 2022 X3NO <X3NO@disroot.org> [https://X3NO.ct8.pl] [https://github.com/X3NOOO]
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# fid is a program to easily access basic information from Faker

import logging
import argparse
from faker import Faker

def generator(country):
    fake = Faker(country)
    
    # Irl
    first_name = fake.first_name()
    logging.debug(f"{first_name=}")
    last_name = fake.last_name()
    logging.debug(f"{last_name=}")
    job = fake.job()
    logging.debug(f"{job=}")

    address = fake.address().replace("\n", ' | ')
    logging.debug(f"{address=}")
    
    # Banking
    ssn = fake.ssn()
    logging.debug(f"{ssn=}")
    bban = fake.bban()
    logging.debug(f"{bban=}")
    iban = fake.iban()
    logging.debug(f"{iban=}")
    swift = fake.swift()
    logging.debug(f"{swift=}")
    
    cc_provider = fake.credit_card_provider()
    logging.debug(f"{cc_provider=}")
    cc_number = fake.credit_card_number()
    logging.debug(f"{cc_number=}")
    cc_cvc = fake.credit_card_security_code()
    logging.debug(f"{cc_cvc=}")
    
    # Technology
    user_agent = fake.user_agent()
    logging.debug(f"{user_agent=}")
    mac = fake.mac_address()
    logging.debug(f"{mac=}")
    login = fake.user_name()
    logging.debug(f"{login=}")
    password = fake.password(length=32)
    logging.debug(f"{password=}")
    
    whole = f'''
WARNING: FOLLOWING INFORMATION ARE FICTIONAL AND
         ANY RESEMBLANCE TO REAL PERSONS IS COINCIDENTAL
         REMEMBER THAT IDENTITY THEFT IS A SERIOUS CRIME

    Personal
---------------
 first name : {first_name}
  last name : {last_name}
    address : {address}
        job : {job}

    Banking
---------------
   provider : {cc_provider}
     number : {cc_number}
        cvc : {cc_cvc}
       iban : {iban}
       bban : {bban}
        ssn : {ssn}
      swift : {swift}

   Technology
---------------
 user agent : {user_agent}
        mac : {mac}
      login : {login}
   password : {password}

WARNING: FOLLOWING INFORMATION ARE FICTIONAL AND
         ANY RESEMBLANCE TO REAL PERSONS IS COINCIDENTAL
         REMEMBER THAT IDENTITY THEFT IS A SERIOUS CRIME'''
    print(whole)
    
    
def main():
    # Parse flags, set default country="random"
    parser = argparse.ArgumentParser(description="fid is a program to easily access basic information from Faker")
    parser.add_argument("country", nargs='*', default="en_US", type=str, help="country that you want to have results from (default: en_US)")
    parser.add_argument("--debug", default=False, type=bool, help="enable debug logs")
    args = parser.parse_args()
    country = args.country
    debug = args.debug
    
    # Set up logging
    if(debug): logging.basicConfig(encoding="utf-8", level=logging.DEBUG)
    else: logging.basicConfig(encoding="utf-8", level=logging.WARNING)
    
    logging.debug(f"{args=}")
    
    # Launch generator with country arg
    generator(country)


if(__name__ == "__main__"):
    main()
