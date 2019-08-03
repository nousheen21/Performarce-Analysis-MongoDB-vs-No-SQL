import random
import string
import math

class Data_Generator():

    """
    Generates profile according to given names.
    Different attributes generated randomly.
    """
    
    def __init__(self, limit):
        
        self.limit = limit
        self.mul = math.ceil(limit/350000)
            
        self.marital_status = {
            1: 'Single',
            2: 'Married',
            3: 'Widowed',
            4: 'Devorced'
        }

        self.profession = {
            1: "Farmer",
            2: "Postman",
            3: "Peon",
            4: "Chef",
            5: "Salesman",
            6: "Social Worker",
            7: "Free lancer",
            8: "Media Worker",
            9: "Minister",   
            10: "Politician",
            11: "Government Officer",
            12: "Artist",
            13: "Entreprenuer",
            14: "Army Officer",
            15: "Athlete",
            16: "Judge",
            17: "Journalist",
            18: "Businessman",
            19: "Teacher",
            20: "Service Holder",
            21: "Student",
        }
        
        self.not_ssc = list(self.profession.values())[0:4]
        self.not_hsc = list(self.profession.values())[0:5]
        self.not_ug = list(self.profession.values())[0:8]
        self.not_grad = list(self.profession.values())[0:10]
        self.not_phd = list(self.profession.values())[0:16]
        
        self.salary = {
            "Service Holder" : [40000, 50000],
            "Businessman": [80000, 200000],
            "Teacher": [15000, 30000],
            "Salesman": [10000, 25000],
            "Farmer": [5000, 10000],
            "Minister": [60000, 80000],
            "Athlete": [10000, 50000],
            "Postman": [5000, 9000],
            "Peon": [5000, 9000],
            "Government Officer": [45000, 60000],
            "Army Officer": [45000, 60000],
            "Artist": [10000, 50000],
            "Entreprenuer": [80000, 500000],
            "Politician": [10000, 50000],
            "Chef": [15000, 30000],
            "Judge": [10000, 50000],
            "Journalist": [15000, 30000],
            "Social Worker": [15000, 30000],
            "Free lancer": [15000, 30000],
            "Media Worker": [15000, 30000],
            "Student": [0, 0]
        }
        
        self.email = {
            1: '@gmail.com',
            2: '@yahoo.com',
            3: '@outlook.com'
        }

        self.mobile_no = {
            1: '019',
            2: '017',
            3: '018',
            4: '015',
            5: '016'
        }

        self.divisions = {
           1: "Barisal",
           2: "Chittagong",
           3: "Dhaka",
           4: "Khulna",
           5: "Rajshahi",
           6: "Mymensingh",
           7: "Rangpur",
           8: "Sylhet",  
        }
        
        self.districts = {
            1: ['Barisal', 'Barguna', 'Bhola', 'Jhalokati', 'Patuakhali', 'Pirojpur'],
            2: ['Brahmanbaria', 'Comilla', 'Chandpur', 'Lakshmipur', 'Noakhali', 'Feni'],
            3: ['Dhaka', 'Gazipur', 'Kishoreganj', 'Manikganj', 'Narayanganj', 'Gopalganj'],    
            4: ['Bagerhat', 'Chuadanga', 'Jessore', 'Jhenaidah', 'Khulna', 'Kushtia'],
            5: ['Bogura', 'Chapainawabganj', 'Joypurhat', 'Naogaon', 'Natore', 'Rajshahi'],
            6: ['Jamalpur', 'Mymensingh', 'Netrokona', 'Sherpur'],
            7: ['Thakurgaon', 'Rangpur', 'Panchagarh', 'Nilphamari', 'Lalmonirhat', 'Kurigram'],
            8: ['Habiganj', 'Moulvibazar', 'Sunamganj', 'Sylhet'],
        }
        
        self.thanas = {
            'Dhaka' : ['Motijheel', 'Mirpur', 'Badda', 'Kotwali', 'Tejgaon'],
            'Chittagong' : ['Rouzan', 'Patiya', 'Mirsharai', 'Barura', 'Fatikchhari'],
            'Barisal' : ['Amtali', 'Betagi', 'Patharghata', 'Agailzhara', 'Babuganj'],
            'Khulna' : ['Chitalmari', 'Fakirhat', 'Kachua', 'Mollahat', 'Rampal'],
            'Rajshahi' : ['Dhunat', 'Gabtoli', 'kalai', 'Ahsanganj', 'Nitpur'],
            'Mymensingh' : ['Bhaluka', 'Shorishabari', 'Gaforgaon', 'Haluaghat', 'Muktagachha'],
            'Rangpur': ['Kaunia', 'Gangachara', 'Mithapukur', 'Saidpur', 'Jaldhaka'],
            'Sylhet' : ['Kalauk', 'Bahubal', 'Madhabpur', 'Nabiganj', 'Kulaura'],
        }
        
        self.villages = {
            'Dhaka' : ['Bagra', 'Dingamanik', 'Haridaspur', 'Goalgram', 'Fardabad'],
            'Chittagong' : ['Baria', 'Aitpara', 'Dhumdumia', 'Ramnagar', 'Harbang '],
            'Barisal' : ['Durga Sagar', 'Gabkhan', 'Ratnopur', 'Goila', 'Kathira'],
            'Khulna' : ['Payari', 'Rajapur', 'Sarankhola', 'Dumuria', 'Rupsa'],
            'Rajshahi' : ['Nagar', 'Bhatahar', 'Paikpara', 'Dhopapara', 'Haribhanga'],
            'Mymensingh' : ['Ujalhati', 'Trishal', 'Phulpur', 'Bahadurpur', 'Nandail'],
            'Rangpur': ['Badarganj ', 'Palash Kandi', 'Panchanan Barma', 'Mistry Para', 'Dahala'],
            'Sylhet' : ['Jahidpur', 'Sujaul', 'Balaganj', 'Jotyintapur', 'Sagarnal '],
        }
        
        self.school_college = ['Adamjee Cantonment Public', 'Rajuk Uttara', 'Cambrian', \
                       'Bogra Zilla', 'Chittagong Cantonment', \
                       'St. Joseph', 'St. Gragery', 'Comilla Cantonment', 'Shaheen',\
                       'Ranpur Zilla', 'Bangladesh Navy', 'City', 'Dhaka']
        
        self.university = ['DU', 'RU', 'CU', 'KU', 'NYU', 'Texas Tech',\
                           'BUET', 'CUET', 'RUET', 'KUET'\
                           'NSU', 'IUB', 'AIUB', 'MIST', \
                           'Harvard', 'MIT', 'Oxford', 'Caltech']
        
        self.default_female_names = {
            'first' : ['Afsana', 'Khadija', 'Maimuna', 'Nafisa', 'Rehnuma'],
            'middle': ['Ara', ' ', 'Binte', 'Umme'],
            'last': ['Hoque', 'begum', 'Haque', 'Kabir']
            
        }
        
        self.default_male_names = {
            'first' : ['Ahmed', 'Kamal', 'Jamal'],
            'middle': [' ', 'Ibne'],
            'last': ['Haque', 'Sarker']
            
        }
               
        self.new_generated_first_names = []
        self.new_generated_middle_names = []
        self.new_generated_last_names = []
        
        self.new_generated_fathers_first_name = []
        self.new_generated_fathers_middle_name = []
        self.new_generated_fathers_last_name = []
        
        self.new_generated_mothers_first_name = []
        self.new_generated_mothers_middle_name = []
        self.new_generated_mothers_last_name = []
        
        self.new_generated_sex = []
        self.new_generated_religion = []
        self.new_generated_marital_status = []
        self.new_generated_profession = []
        self.new_generated_DOB = []
        
        self.new_generated_emails = []
        self.new_generated_mobile_no = []
        
        self.new_generated_height = []
        self.new_generated_weight = []
        
        self.new_generated_salary = []
        self.new_generated_tin_no = []
        self.new_generated_income_tax = []
        self.new_generated_assets = []
        
        self.new_generated_school = []
        self.new_generated_SSC_gpa = []
        self.new_generated_college = []
        self.new_generated_HSC_gpa = []
        self.new_generated_ug = []
        self.new_generated_ug_cgpa = []
        self.new_generated_grad = []
        self.new_generated_grad_cgpa = []
        self.new_generated_phd = []

        self.new_generated_permanent_addr_house_no = []
        self.new_generated_permanent_addr_street_no = []
        self.new_generated_permanent_addr_word_no = []
        self.new_generated_permanent_addr_village = []
        self.new_generated_permanent_addr_thana = []
        self.new_generated_permanent_addr_city = []
        self.new_generated_permanent_addr_district = []
        self.new_generated_permanent_addr_division = []
        
        self.new_generated_present_addr_house_no = []
        self.new_generated_present_addr_street_no = []
        self.new_generated_present_addr_word_no = []
        self.new_generated_present_addr_village = []
        self.new_generated_present_addr_thana = []
        self.new_generated_present_addr_city = []
        self.new_generated_present_addr_district = []
        self.new_generated_present_addr_division = []
        
        
        self.new_generated_place_of_birth = []
        self.new_generated_NID = []
        self.new_generated_passport_no = []
        
        self.new_generated_ec_firstname = []
        self.new_generated_ec_middlename = []
        self.new_generated_ec_lastname = []
        self.new_generated_ec_mobile = []
        self.new_generated_ec_email = []
        self.new_generated_ec_permanent_addr_house_no = []
        self.new_generated_ec_permanent_addr_street_no = []
        self.new_generated_ec_permanent_addr_word_no = []
        self.new_generated_ec_permanent_addr_village = []
        self.new_generated_ec_permanent_addr_thana = []
        self.new_generated_ec_permanent_addr_city = []
        self.new_generated_ec_permanent_addr_district = []
        self.new_generated_ec_permanent_addr_division = []
        self.new_generated_ec_present_addr_house_no = []
        self.new_generated_ec_present_addr_street_no = []
        self.new_generated_ec_present_addr_word_no = []
        self.new_generated_ec_present_addr_village = []
        self.new_generated_ec_present_addr_thana = []
        self.new_generated_ec_present_addr_city = []
        self.new_generated_ec_present_addr_district = []
        self.new_generated_ec_present_addr_division = []
        
        for i in range(5):
            self.new_generated_first_names.append("Ahmed")
            self.new_generated_middle_names.append("Reza")
            self.new_generated_last_names.append("Haque")
            self.new_generated_NID.append(self.generate_NID())
            self.new_generated_passport_no.append(self.generate_passport_no())
            self.new_generated_sex.append("male")
            self.new_generated_religion.append("muslim")
            self.new_generated_marital_status.append("Single")
            
            dob, age = self.generate_DOB()
            
            if age <= 22:
                prof = "Student"
            else:
                prof = self.profession[random.randint(1, 21)]
            
            self.new_generated_profession.append(prof)
            
            self.new_generated_DOB.append(dob)
            
            self.new_generated_height.append(str(random.randint(4, 6)) + "ft. " + str(random.randint(1, 11)) + " inches")
            self.new_generated_weight.append(str(random.randint(80, 120)) + " lbs")
            
            salary= self.generate_salary(prof)
            self.new_generated_salary.append(salary)
            self.new_generated_tin_no.append(self.generate_tin_no(salary))
            
            school, result = self.generate_SSC(prof, age)
            self.new_generated_school.append(school)
            self.new_generated_SSC_gpa.append(result)
            
            college, result1 = self.generate_HSC(prof, age)
            self.new_generated_college.append(college)
            self.new_generated_HSC_gpa.append(result1)
            
            
            university, result2 = self.generate_UG(prof, age)
            self.new_generated_ug.append(university)
            self.new_generated_ug_cgpa.append(result2)
           
            university1, result3 = self.generate_Grad(prof, age)
            self.new_generated_grad.append(university1)
            self.new_generated_grad_cgpa.append(result3)
            
            result4 = self.generate_PhD(prof, age)
            self.new_generated_phd.append(result4)
            
            self.new_generated_assets.append(self.generate_assets(salary))
            
            self.new_generated_income_tax.append(self.generate_income_tax(salary))
            self.new_generated_emails.append(self.generate_email("Ahmed", "Reza"))
            self.new_generated_mobile_no.append(self.generate_phone_no())
            
            self.generate_permanent_present_address()
            
            self.new_generated_fathers_first_name.append(random.choice(self.default_male_names['first']))
            self.new_generated_fathers_middle_name.append(random.choice(self.default_male_names['middle']))
            self.new_generated_fathers_last_name.append(random.choice(self.default_male_names['last']))
            self.new_generated_mothers_first_name.append(random.choice(self.default_female_names['first']))
            self.new_generated_mothers_middle_name.append(random.choice(self.default_female_names['middle']))
            self.new_generated_mothers_last_name.append(random.choice(self.default_female_names['last']))
            self.new_generated_place_of_birth.append(random.choice(self.districts[random.randint(1, 4)]))
            
            ec_fname = random.choice(self.default_male_names['first'])
            ec_lname = random.choice(self.default_male_names['last'])
            self.new_generated_ec_firstname.append(ec_fname)
            self.new_generated_ec_middlename.append(random.choice(self.default_male_names['middle']))
            self.new_generated_ec_lastname.append(ec_lname)
            self.new_generated_ec_mobile.append(self.generate_phone_no())
            self.new_generated_ec_email.append(self.generate_email(ec_fname, ec_lname))

    def get_data(self):
        Data = {'First name': self.new_generated_first_names[:self.limit],
                'Middle name': self.new_generated_middle_names[:self.limit],
                'Last name': self.new_generated_last_names[:self.limit],
                'NID': self.new_generated_NID[:self.limit],
                'Fathers First Name': self.new_generated_fathers_first_name[:self.limit],
                'Fathers Middle Name': self.new_generated_fathers_middle_name[:self.limit],
                'Fathers Last Name': self.new_generated_fathers_last_name[:self.limit],
                'Mothers First Name': self.new_generated_mothers_first_name[:self.limit],
                'Mothers Middle Name': self.new_generated_mothers_middle_name[:self.limit],
                'Mothers Last Name': self.new_generated_mothers_last_name[:self.limit],
                'Sex': self.new_generated_sex[:self.limit],
                'Religion': self.new_generated_religion[:self.limit],
                'Marital Status': self.new_generated_marital_status[:self.limit],
                'Height': self.new_generated_height[:self.limit],
                'Weight': self.new_generated_weight[:self.limit],
                'Profession': self.new_generated_profession[:self.limit],
                'Income': self.new_generated_salary[:self.limit],
                'Income Tax' : self.new_generated_income_tax[:self.limit],
                'TIN No': self.new_generated_tin_no[:self.limit],
                'Assets': self.new_generated_assets[:self.limit],
                'Date of Birth': self.new_generated_DOB[:self.limit],
                'Passport No': self.new_generated_passport_no[:self.limit],
                'Email Address': self.new_generated_emails[:self.limit],
                'Mobile No': self.new_generated_mobile_no[:self.limit],
                'Prsnt_addr_house_no': self.new_generated_present_addr_house_no[:self.limit],
                'Prsnt_addr_street_no': self.new_generated_present_addr_street_no[:self.limit],
                'Prsnt_addr_ward_no': self.new_generated_present_addr_word_no[:self.limit],
                'Prsnt_addr_village': self.new_generated_present_addr_village[:self.limit],
                'Prsnt_addr_thana': self.new_generated_present_addr_thana[:self.limit],
                'Prsnt_addr_city': self.new_generated_present_addr_city[:self.limit],
                'Prsnt_addr_district': self.new_generated_present_addr_district[:self.limit],
                'Prsnt_addr_division': self.new_generated_present_addr_division[:self.limit],                
                'Prmntn_addr_house_no': self.new_generated_permanent_addr_house_no[:self.limit],
                'Prmntn_addr_street_no': self.new_generated_permanent_addr_street_no[:self.limit],
                'Prmntn_addr_ward_no': self.new_generated_permanent_addr_word_no[:self.limit],
                'Prmntn_addr_village': self.new_generated_permanent_addr_village[:self.limit],
                'Prmntn_addr_thana': self.new_generated_permanent_addr_thana[:self.limit],
                'Prmntn_addr_city': self.new_generated_permanent_addr_city[:self.limit],
                'Prmntn_addr_district': self.new_generated_permanent_addr_district[:self.limit],
                'Prmntn_addr_division': self.new_generated_permanent_addr_division[:self.limit],
                'SSC Passed From': self.new_generated_school[:self.limit],
                'SSC Result': self.new_generated_SSC_gpa[:self.limit],
                'HSC Passed From': self.new_generated_college[:self.limit],
                'HSC Result': self.new_generated_HSC_gpa[:self.limit],
                'Graduated From': self.new_generated_ug[:self.limit],
                'Undergrad Result': self.new_generated_ug_cgpa[:self.limit],
                'Post Graduated From': self.new_generated_grad[:self.limit],
                'Postgrad Result': self.new_generated_grad_cgpa[:self.limit],
                'Doctorate From': self.new_generated_phd[:self.limit],
                'Place of Birth': self.new_generated_place_of_birth[:self.limit],
                'EC First Name': self.new_generated_ec_firstname[:self.limit],
                'EC Middle Name': self.new_generated_ec_middlename[:self.limit],
                'EC Last Name': self.new_generated_ec_lastname[:self.limit],
                'EC_Prsnt_addr_house_no': self.new_generated_ec_present_addr_house_no[:self.limit],
                'EC_Prsnt_addr_street_no': self.new_generated_ec_present_addr_street_no[:self.limit],
                'EC_Prsnt_addr_ward_no': self.new_generated_ec_present_addr_word_no[:self.limit],
                'EC_Prsnt_addr_village': self.new_generated_ec_present_addr_village[:self.limit],
                'EC_Prsnt_addr_thana': self.new_generated_ec_present_addr_thana[:self.limit],
                'EC_Prsnt_addr_city': self.new_generated_ec_present_addr_city[:self.limit],
                'EC_Prsnt_addr_district': self.new_generated_ec_present_addr_district[:self.limit],
                'EC_Prsnt_addr_division': self.new_generated_ec_present_addr_division[:self.limit],                
                'EC_Prmntn_addr_house_no': self.new_generated_ec_permanent_addr_house_no[:self.limit],
                'EC_Prmntn_addr_street_no': self.new_generated_ec_permanent_addr_street_no[:self.limit],
                'EC_Prmntn_addr_ward_no': self.new_generated_ec_permanent_addr_word_no[:self.limit],
                'EC_Prmntn_addr_village': self.new_generated_ec_permanent_addr_village[:self.limit],
                'EC_Prmntn_addr_thana': self.new_generated_ec_permanent_addr_thana[:self.limit],
                'EC_Prmntn_addr_city': self.new_generated_ec_permanent_addr_city[:self.limit],
                'EC_Prmntn_addr_district': self.new_generated_ec_permanent_addr_district[:self.limit],
                'EC_Prmntn_addr_division': self.new_generated_ec_permanent_addr_division[:self.limit],
                'EC Mobile No': self.new_generated_ec_mobile[:self.limit],
                'EC Email Address': self.new_generated_ec_email[:self.limit],
                }
        
        columns = ['First name', 'Middle name', 'Last name', 'NID', 'Fathers First Name', \
                   'Fathers Middle Name', 'Fathers Last Name', 'Mothers First Name', \
                   'Mothers Middle Name', 'Mothers Last Name', 'Sex', 'Religion', \
                   'Marital Status', 'Height', 'Weight', 'Profession', 'Income', \
                   'Income Tax', 'TIN No', 'Assets', 'Date of Birth', 'Passport No', 'Email Address',\
                   'Mobile No', 'Prsnt_addr_house_no', 'Prsnt_addr_street_no', 'Prsnt_addr_ward_no', \
                   'Prsnt_addr_village', 'Prsnt_addr_thana', 'Prsnt_addr_city', 'Prsnt_addr_district', \
                   'Prsnt_addr_division', 'Prmntn_addr_house_no', 'Prmntn_addr_street_no', \
                   'Prmntn_addr_ward_no', 'Prmntn_addr_village', 'Prmntn_addr_thana', \
                   'Prmntn_addr_city', 'Prmntn_addr_district', 'Prmntn_addr_division', 'SSC Passed From',\
                   'SSC Result', 'HSC Passed From', 'HSC Result',  'Graduated From',\
                   'Undergrad Result', 'Post Graduated From', 'Postgrad Result',\
                   'Doctorate From',  'Place of Birth', 'EC First Name', 'EC Middle Name',\
                   'EC Last Name', 'EC_Prsnt_addr_house_no', 'EC_Prsnt_addr_street_no', \
                   'EC_Prsnt_addr_ward_no', 'EC_Prsnt_addr_village', 'EC_Prsnt_addr_thana',\
                   'EC_Prsnt_addr_city', 'Prsnt_addr_district','EC_Prsnt_addr_division', \
                    'EC_Prmntn_addr_house_no', 'EC_Prmntn_addr_street_no', \
                   'EC_Prmntn_addr_ward_no', 'EC_Prmntn_addr_village', 'EC_Prmntn_addr_thana', \
                   'EC_Prmntn_addr_city', 'EC_Prmntn_addr_district', 'EC_Prmntn_addr_division', \
                   'EC Mobile No', 'EC Email Address']

        return Data, columns

    def generate_profile(self, first_names, middle_names, last_names, gender, religion):
        for firstname in first_names:
            for lastname in last_names:
                if middle_names != None:
                    for middlename in middle_names:
                        for i in range(self.mul):
                            self.generate_single_profile(first_names, last_names, firstname, middlename, lastname, gender, religion)
#                        
                else:
                    for i in range(self.mul):
                        self.generate_single_profile(first_names, last_names, firstname, None, lastname, gender, religion)
             
    def generate_single_profile(self, first_names, last_names, firstname, middlename, lastname, gender, religion):
        self.new_generated_first_names.append(firstname)
        self.new_generated_middle_names.append(middlename)
        self.new_generated_last_names.append(lastname)       
        self.new_generated_NID.append(self.generate_NID())
        self.new_generated_passport_no.append(self.generate_passport_no())
        self.new_generated_sex.append(gender)
        self.new_generated_religion.append(religion)
        self.new_generated_marital_status.append(self.marital_status[random.randint(1, 4)])
        
        dob, age = self.generate_DOB()
        if age <= 22:
                prof = "Student"
        else:
                prof = self.profession[random.randint(1, 21)]
                
        self.new_generated_profession.append(prof)
        
        self.new_generated_height.append(str(random.randint(4, 6)) + " ft. " + str(random.randint(1, 11)) + " inches")
        self.new_generated_weight.append(str(random.randint(80, 120)) + " lbs")
            
        self.new_generated_DOB.append(dob)
        
        salary= self.generate_salary(prof)
        self.new_generated_salary.append(salary)
        self.new_generated_tin_no.append(self.generate_tin_no(salary))
        
        school, result = self.generate_SSC(prof, age)
        self.new_generated_school.append(school)
        self.new_generated_SSC_gpa.append(result)
        
        college, result1 = self.generate_HSC(prof, age)
        self.new_generated_college.append(college)
        self.new_generated_HSC_gpa.append(result1)
        
        university, result2 = self.generate_UG(prof, age)
        self.new_generated_ug.append(university)
        self.new_generated_ug_cgpa.append(result2)
       
        university1, result3 = self.generate_Grad(prof, age)
        self.new_generated_grad.append(university1)
        self.new_generated_grad_cgpa.append(result3)
        
        result4 = self.generate_PhD(prof, age)
        self.new_generated_phd.append(result4)
            
        self.new_generated_assets.append(self.generate_assets(salary))
        self.new_generated_income_tax.append(self.generate_income_tax(salary))
        self.new_generated_emails.append(self.generate_email(firstname, lastname))
        self.new_generated_mobile_no.append(self.generate_phone_no())
        
        self.generate_permanent_present_address()
        
        fname, mname, lname = self.get_fathers_name(first_names, middlename, lastname, gender)
        self.new_generated_fathers_first_name.append(fname)
        self.new_generated_fathers_middle_name.append(mname)
        self.new_generated_fathers_last_name.append(lname)
        fname1, mname1, lname1 = self.get_mothers_name(first_names, last_names, middlename, gender)
        self.new_generated_mothers_first_name.append(fname1)
        self.new_generated_mothers_middle_name.append(mname1)
        self.new_generated_mothers_last_name.append(lname1)
        self.new_generated_place_of_birth.append(random.choice(self.districts[random.randint(1, 4)]))
    
        ec_fname = random.choice(first_names)
        ec_lname = random.choice(last_names)
        self.new_generated_ec_firstname.append(ec_fname)
        self.new_generated_ec_middlename.append(middlename)
        self.new_generated_ec_lastname.append(ec_lname)
        self.new_generated_ec_mobile.append(self.generate_phone_no())
        self.new_generated_ec_email.append(self.generate_email(ec_fname, ec_lname))
        
    def generate_salary(self, prof):
        lower, upper = self.salary[prof]
        return random.randint(lower, upper)
        
    def generate_passport_no(self):
        pass_no = None
        
        if random.randint(1, 4) is not 4:
            str1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
                   str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
                   str(random.randint(0, 9))
            str2 = random.choice(string.ascii_letters[0:4]).upper() + random.choice(string.ascii_letters).upper()    
            pass_no = str2 + str1
        
        return pass_no
        
    def generate_SSC(self, prof, age):
        school = None
        result = ''
        
        if prof not in self.not_ssc and age >= 16:
            school = random.choice(self.school_college) + " School"
            if random.randint(1, 2) % 2 == 0:
                result = str(5.00)
            else:
                result = str(random.randint(300, 500) / 100)
            
        return school, result
    
    def generate_HSC(self, prof, age):
        school = None
        result = ''
        
        if prof not in self.not_hsc and age >= 18:
            school = random.choice(self.school_college) + " College"
            if random.randint(1, 2) % 2 == 0:
                result = str(5.00)
            else:
                result = str(random.randint(300, 500) / 100)
            
        return school, result
    
    def generate_UG(self, prof, age):
        school = None
        result = ''
        
        if prof not in self.not_ug and age >= 22:
            school = random.choice(self.university)
            result = str(random.randint(200, 400) / 100)
            
        return school, result
    
    def generate_Grad(self, prof, age):
        school = None
        result = ''
        
        if prof not in self.not_grad and age >= 24:
            school = random.choice(self.university)
            result = str(random.randint(200, 400) / 100)
            
        return school, result
    
    def generate_PhD(self, prof, age):
        school = None
        
        if prof not in self.not_phd and age >= 28:
            school = random.choice(self.university)
            
        return school
        
    def generate_email(self, firstname, lastname):
        email = None
        if random.randint(1, 10) % 2 == 0:
           email = firstname.lower() + "." + lastname.lower() + self.email[random.randint(1, 3)]
    
        return email
    
    def get_fathers_name(self, firstnames, middlename, lastname, gender):
        fname = None
        mname = None
        lname = None
        if gender is 'male':
            fname = random.choice(firstnames) 
            mname = middlename 
            lname = lastname
        else:
            fname = random.choice(self.new_generated_fathers_first_name)
            mname = random.choice(self.new_generated_fathers_middle_name)
            lname = random.choice(self.new_generated_fathers_last_name)
        
        return fname, mname, lname
        
    def get_mothers_name(self, firstnames, lastnames, middlename, gender):
        fname = None
        mname = None
        lname = None
        if gender is 'female':
            fname = random.choice(firstnames) 
            lname = random.choice(lastnames) 
            mname = middlename
        else:
            if len(self.new_generated_mothers_first_name) > 0 and \
                len(self.new_generated_mothers_middle_name) > 0 and \
                len(self.new_generated_mothers_last_name) > 0 :
                fname = random.choice(self.new_generated_mothers_first_name)
                mname = random.choice(self.new_generated_mothers_middle_name)
                lname = random.choice(self.new_generated_mothers_last_name)
            
        return fname, mname, lname
        
    def generate_tin_no(self, salary):
        tin = None
        if salary >= 25000:
            tin = str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) 
        
        return tin 
    
    def generate_income_tax(self, income):
        tax = 0
        if income >= 25000:
            tax = (income * 30) / 100
            
        return tax
    
    def generate_assets(self, income):
        str1 = ""
        flats = 0
        cars = 0
        plots = 0
        
        if income >= 35000:
            flats += 1
        if income >= 50000:
            cars += 1
        if income >= 75000:
            flats += 1
            plots += 1
        if income >= 100000:
            cars += 1
        if income >= 200000:
            flats += 1
            plots += 1
            cars += 1
            
        if cars > 0:
            str1 += str(cars) + " car(s) "
        if flats > 0:
            str1 += str(flats) + " flat(s) "
        if plots > 0:
            str1 += str(plots) + " plots(s)"
            
        return str1
    
    def generate_permanent_present_address(self):
        City = 0
        Village = 1
        city_or_village = random.randint(0, 1)
        
        if city_or_village is City:
            div = random.randint(1, 7)
            city = random.choice(self.districts[div])
            self.new_generated_permanent_addr_house_no.append(str(random.randint(1, 70)))
            self.new_generated_permanent_addr_street_no.append(str(random.randint(1, 20)))
            self.new_generated_permanent_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_permanent_addr_village.append(' ')
            self.new_generated_permanent_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_permanent_addr_city.append(city)
            self.new_generated_permanent_addr_district.append(city)
            self.new_generated_permanent_addr_division.append(self.divisions[div])
            
            div = random.randint(1, 7)
            city = random.choice(self.districts[div])
            self.new_generated_present_addr_house_no.append(str(random.randint(1, 70)))
            self.new_generated_present_addr_street_no.append(str(random.randint(1, 20)))
            self.new_generated_present_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_present_addr_village.append(' ')
            self.new_generated_present_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_present_addr_city.append(city)
            self.new_generated_present_addr_district.append(city)
            self.new_generated_present_addr_division.append(self.divisions[div])
            
            div = random.randint(1, 7)
            city = random.choice(self.districts[div])
            self.new_generated_ec_permanent_addr_house_no.append(str(random.randint(1, 70)))
            self.new_generated_ec_permanent_addr_street_no.append(str(random.randint(1, 20)))
            self.new_generated_ec_permanent_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_ec_permanent_addr_village.append(' ')
            self.new_generated_ec_permanent_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_ec_permanent_addr_city.append(city)
            self.new_generated_ec_permanent_addr_district.append(city)
            self.new_generated_ec_permanent_addr_division.append(self.divisions[div])
            
            div = random.randint(1, 7)
            city = random.choice(self.districts[div])
            self.new_generated_ec_present_addr_house_no.append(str(random.randint(1, 70)))
            self.new_generated_ec_present_addr_street_no.append(str(random.randint(1, 20)))
            self.new_generated_ec_present_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_ec_present_addr_village.append(' ')
            self.new_generated_ec_present_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_ec_present_addr_city.append(city)
            self.new_generated_ec_present_addr_district.append(city)
            self.new_generated_ec_present_addr_division.append(self.divisions[div])
            
        if city_or_village is Village: 
            div = random.randint(1, 7)
            self.new_generated_permanent_addr_house_no.append(' ')
            self.new_generated_permanent_addr_street_no.append(' ')
            self.new_generated_permanent_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_permanent_addr_village.append(random.choice(self.villages[self.divisions[div]]))
            self.new_generated_permanent_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_permanent_addr_city.append(' ')
            self.new_generated_permanent_addr_district.append(random.choice(self.districts[div]))
            self.new_generated_permanent_addr_division.append(self.divisions[div])
            
            div = random.randint(1, 7)
            self.new_generated_present_addr_house_no.append(' ')
            self.new_generated_present_addr_street_no.append(' ')
            self.new_generated_present_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_present_addr_village.append(random.choice(self.villages[self.divisions[div]]))
            self.new_generated_present_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_present_addr_city.append(' ')
            self.new_generated_present_addr_district.append(random.choice(self.districts[div]))
            self.new_generated_present_addr_division.append(self.divisions[div])
            
            div = random.randint(1, 7)
            self.new_generated_ec_permanent_addr_house_no.append(' ')
            self.new_generated_ec_permanent_addr_street_no.append(' ')
            self.new_generated_ec_permanent_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_ec_permanent_addr_village.append(random.choice(self.villages[self.divisions[div]]))
            self.new_generated_ec_permanent_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_ec_permanent_addr_city.append(' ')
            self.new_generated_ec_permanent_addr_district.append(random.choice(self.districts[div]))
            self.new_generated_ec_permanent_addr_division.append(self.divisions[div])
            
            div = random.randint(1, 7)
            self.new_generated_ec_present_addr_house_no.append(' ')
            self.new_generated_ec_present_addr_street_no.append(' ')
            self.new_generated_ec_present_addr_word_no.append(str(random.randint(1, 70)))
            self.new_generated_ec_present_addr_village.append(random.choice(self.villages[self.divisions[div]]))
            self.new_generated_ec_present_addr_thana.append(random.choice(self.thanas[self.divisions[div]]))
            self.new_generated_ec_present_addr_city.append(' ')
            self.new_generated_ec_present_addr_district.append(random.choice(self.districts[div]))
            self.new_generated_ec_present_addr_division.append(self.divisions[div])
        
    def generate_permanent_address(self):
        ward_no = random.randint(1, 45)
        div = random.randint(1, 7)
        village = random.choice(self.villages[self.divisions[div]])
        thana = random.choice(self.thanas[self.divisions[div]])
        dist = random.choice(self.districts[div])
        division = self.divisions[div]
        
        return "Ward no. " + str(ward_no) +  ", Village name: " + village + \
                ", Thana: " + thana + ", District: " + dist + ", Division: " + division + "."
                
    def generate_DOB(self):
        year = random.randint(1950, 2010)
        age = 2019 - year
        return str(random.randint(1, 28)) + "/" + str(random.randint(1, 12)) + "/" + str(year), age

    def generate_phone_no(self):
        str1 = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9))
               
        return self.mobile_no[random.randint(1, 5)] + str1
    
    def generate_NID(self):
        str1 = str(random.randint(1, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + \
               str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

        return str1
