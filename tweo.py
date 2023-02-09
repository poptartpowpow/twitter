#Twitter Geo
#-----------
#A module for cleaning self-reported Twitter user locations. Error rate = TBD
#NOTE: This is not an exhaustive or comprehensive library. Locations are input by hand to avoid errors, and flow written to control for duplicate place names, where possible. 
#It is written to loop through all possible locations, so that users who report multiple countries will be accounted for. This means that it runs rather slow—but, due to Twitter's rate limits, does not impact overall speed of any large request
#NOTE: users who report multiple locations will skew results


def parse_location(user_location): 

    #Now, we create a blank dictionary: 
    loc_dict = {
        'city': '',
        'state': '', 
        'country': ''
    }

    #CHECK FOR MATCHES WITH LOCATIONS
    def location_iterator(user_location):
        Location = str(user_location)
        location = Location.lower().strip().replace(',', '').replace('.', '') #ThIs Is CaSe SeNsItIvE


        #United States----------------------
        
        #USA
        if ('united states' in location) or (('usa' or 'us') == location) or (('USA') in Location): 
            loc_dict['country'] = 'USA'


        #AK--------------------
        if ('alaska' in location) or ('ak' == location) or ('AK' in Location):
            loc_dict['state'] = 'AK'
            loc_dict['country'] = 'USA'

        if 'anchorage' in location:
            loc_dict['city'] = 'Anchorage'
            loc_dict['state'] = 'AK'
            loc_dict['country'] = 'USA'
        

        #AZ--------------------
        if ('arizona' in location) or ('az' == location) or ('AZ' in Location):
            loc_dict['state'] = 'AZ'
            loc_dict['country'] = 'USA'

        if ('phoenix az' or 'phoenix arizona') in location:
            loc_dict['city'] = 'Phoenix'
            loc_dict['state'] = 'AZ'
            loc_dict['country'] = 'USA'
        if ('flagstaff az' or 'flagstaff arizona') in location:
            loc_dict['city'] = 'Flagstaff'
            loc_dict['state'] = 'AZ'
            loc_dict['country'] = 'USA'


        #CA-------------------------
        if ('california' in location) or ('ca' == location) or ('CA' in Location):
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'

        if ('los angeles') in location:
            loc_dict['city'] = 'Los Angeles'
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if 'la' == location:
            loc_dict['city'] = 'Los Angeles'
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if ('san francisco' or 'san fran' or 'sanfran' or 'frisco') in location:
            loc_dict['city'] = 'San Francisco'            
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if 'truckee' in location:
            loc_dict['city'] = 'Truckee'
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if 'south lake tahoe' in location:
            loc_dict['city'] = 'South Lake Tahoe'
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if 'san diego' in location:
            loc_dict['city'] = 'San Diego'
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if 'sacremento' in location:
            loc_dict['city'] = 'Sacremento'
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'
        if ('sf bay') in location:
            loc_dict['state'] = 'CA'
            loc_dict['country'] = 'USA'


        #CO------------------------
        if ('colorado' in location) or ('co' == location) or ('CO' in Location):
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'

        if 'denver' in location:
            loc_dict['city'] = 'Denver'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'boulder' in location:
            loc_dict['city'] = 'Boulder'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'colorado springs' in location:
            loc_dict['city'] = 'Colorado Springs'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'golden co' in location:
            loc_dict['city'] = 'Golden'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'carbondale' in location:
            loc_dict['city'] = 'Carbondale'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'wheat ridge co' in location:
            loc_dict['city'] = 'Carbondale'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'vail' in location:
            loc_dict['city'] = 'Vail'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'telluride' in location:
            loc_dict['city'] = 'Telluride'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'steamboat springs' in location:
            loc_dict['city'] = 'Steamboat Springs'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'superior co' in location:
            loc_dict['city'] = 'Superior'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'fort collins' in location:
            loc_dict['city'] = 'Fort Collins'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'breckenridge' in location:
            loc_dict['city'] = 'Breckenridge'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'aspen' in location:
            loc_dict['city'] = 'Aspen'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        if 'crested butte' in location:
            loc_dict['city'] = 'Crested Butte'
            loc_dict['state'] = 'CO'
            loc_dict['country'] = 'USA'
        

        #DC----------------
        if ('dc' == location) or (('washington dc' or 'district of columbia') in location) or ('DC' in Location):
            loc_dict['city'] = 'Washington, DC'
            loc_dict['state'] = 'DC'
            loc_dict['country'] = 'USA'

        
        #FL--------------------
        if ('florida' in location) or ('fl' == location) or ('FL' in Location):
            loc_dict['state'] = 'FL'
            loc_dict['country'] = 'USA'

        if 'miami' in location:
            loc_dict['city'] = 'Miami'            
            loc_dict['state'] = 'FL'
            loc_dict['country'] = 'USA'


        #Georgia-----------------
        if ('GA' in Location):
            loc_dict['state'] = 'GA'
            loc_dict['country'] = 'USA'
        if 'atlanta' in location: 
            loc_dict['city'] = 'Atlanta'            
            loc_dict['state'] = 'GA'
            loc_dict['country'] = 'USA'
        
        #ID----------------------
        if ('idaho' in location) or ('ID' in Location):
            loc_dict['state'] = 'ID'
            loc_dict['country'] = 'USA'

        if 'boise' in location:
            loc_dict['city'] = 'Boise'            
            loc_dict['state'] = 'ID'
            loc_dict['country'] = 'USA'
        if ('sun valley id' or 'sun valley idaho') in location:
            loc_dict['city'] = 'Sun Valley'            
            loc_dict['state'] = 'ID'
            loc_dict['country'] = 'USA'
        
        #IL-----------------------
        if ('illinois' in location) or ('IL' in Location):
            loc_dict['state'] = 'IL'
            loc_dict['country'] = 'USA'
        if 'chicago' in location:
            loc_dict['city'] = 'Chicago'            
            loc_dict['state'] = 'IL'
            loc_dict['country'] = 'USA'

        
        #MA---------------------
        if ('massachusetts' in location) or ('MA' in Location): 
            loc_dict['state'] = 'MA'
            loc_dict['country'] = 'USA'  

        if 'boston' in location: 
            loc_dict['city'] = 'Boston'            
            loc_dict['state'] = 'MA'
            loc_dict['country'] = 'USA'
        if 'cambridge' in location:
            loc_dict['city'] = 'Cambridge'            
            loc_dict['state'] = 'MA'
            loc_dict['country'] = 'USA'
        if 'seattle' in location:
            loc_dict['city'] = 'Seattle'            
            loc_dict['state'] = 'WA'
            loc_dict['country'] = 'USA'

        
        #MD-----------------------
        if ('maryland' in location) or ('MD' in Location): 
            loc_dict['state'] = 'MD'
            loc_dict['country'] = 'USA' 

        if 'bethesda md' in location:
            loc_dict['city'] = 'Bethesda'            
            loc_dict['state'] = 'MD'
            loc_dict['country'] = 'USA'  
        if 'baltimore' in location:
            loc_dict['city'] = 'Baltimore'            
            loc_dict['state'] = 'MD'
            loc_dict['country'] = 'USA'  


        #ME----------------------
        if ('maine' in location) or ('ME' in Location):
            loc_dict['state'] = 'ME'
            loc_dict['country'] = 'USA'


        #MI----------------------
        if ('michigan' in location) or ('MI' in Location):
            loc_dict['state'] = 'MI'
            loc_dict['country'] = 'USA'


        #MN-----------------------
        if ('minnesota' in location) or ('MN' in Location):
            loc_dict['state'] = 'MN'
            loc_dict['country'] = 'USA'

        if 'st paul mn' in location:
            loc_dict['city'] = 'St. Paul'
            loc_dict['state'] = 'MN'
            loc_dict['country'] = 'USA'
        
        
        #MT---------------------
        if ('montana' in location) or ('mt' == location) or ('MT' in Location):
            loc_dict['state'] = 'MT'
            loc_dict['country'] = 'USA'

        if 'bozeman' in location: 
            loc_dict['city'] = 'Bozeman'
            loc_dict['state'] = 'MT'
            loc_dict['country'] = 'USA'
        if 'whitefish' in location: 
            loc_dict['city'] = 'Bozeman'
            loc_dict['state'] = 'MT'
            loc_dict['country'] = 'USA'
        if 'missoula' in location: 
            loc_dict['city'] = 'Missoula'
            loc_dict['state'] = 'MT'
            loc_dict['country'] = 'USA'


        #NH--------------------------
        if ('new hampshire' in location) or ('NH' in Location): 
            loc_dict['state'] = 'NH'
            loc_dict['country'] = 'USA'


        #NJ--------------------------
        if ('new jersey' in location) or ('NJ' in Location): 
            loc_dict['state'] = 'NJ'
            loc_dict['country'] = 'USA'

        if 'princeton' in location:
            loc_dict['city'] = 'Princeton'                        
            loc_dict['state'] = 'NJ'
            loc_dict['country'] = 'USA'
        

        #NC---------------------------
        if ('north carolina' in location) or ('NC' in Location):
            loc_dict['state'] = 'NC'
            loc_dict['country'] = 'USA'

        if ('charlotte nc' or 'charlotte north carolina') in location:
            loc_dict['city'] = 'Charlotte'                        
            loc_dict['state'] = 'NC'
            loc_dict['country'] = 'USA'
        
        
        #NM------------------------
        if ('new mexico' in location) or ('NM' in Location):
            loc_dict['state'] = 'NM'
            loc_dict['country'] = 'USA'

        if 'alburquerque' in location:
            loc_dict['city'] = 'Alburquerque'                        
            loc_dict['state'] = 'NM'
            loc_dict['country'] = 'USA'

        #NV----------------------
        if ('nevada' in location) or ('NV' in Location): 
            loc_dict['state'] = 'NV'    
            loc_dict['country'] = 'USA'
        if ('reno') in location:
            loc_dict['city'] = 'Reno'        
            loc_dict['state'] = 'NV'
            loc_dict['country'] = 'USA'


        #NY-----------------------
        if ('new york' in location) or ('ny' == location) or ('NY' in Location):
            loc_dict['state'] = 'NY'
            loc_dict['country'] = 'USA'

        if ('nyc' or 'new york city' or 'ny city' or 'brooklyn' or 'queens' or 'staten island' or 'manhattan' or 'bronx') in location:
            loc_dict['city'] = 'New York City'
            loc_dict['state'] = 'NY'
            loc_dict['country'] = 'USA'
        if ('syracuse') in location:
            loc_dict['city'] = 'Syracuse'
            loc_dict['state'] = 'NY'
            loc_dict['country'] = 'USA'
        

        #OH----------------------
        if ('ohio' in location) or ('OH' in Location):
            loc_dict['state'] = 'OH'
            loc_dict['country'] = 'USA'

        #OR-----------------------
        if ('oregon' in location) or ('or' == location) or ('OR' in Location): 
            loc_dict['state'] = 'OR'
            loc_dict['country'] = 'USA'
        
        if 'portland or' in location: 
            loc_dict['city'] = 'portland'
            loc_dict['state'] = 'OR'
            loc_dict['country'] = 'USA'
        if ('bend or' or 'bend oregon') in location: 
            loc_dict['city'] = 'portland'
            loc_dict['state'] = 'OR'
            loc_dict['country'] = 'USA'


        #PA--------------------------
        if ('pennsylvania' in location) or ('pa' == location) or ('PA' in Location):
            loc_dict['state'] = 'PA'
            loc_dict['country'] = 'USA'

        if 'philadelphia' in location:
            loc_dict['city'] = 'Philadelphia'                        
            loc_dict['state'] = 'PA'
            loc_dict['country'] = 'USA'


        #SC---------------------------
        if ('south carolina' in location) or ('SC' in Location):
            loc_dict['state'] = 'SC'
            loc_dict['country'] = 'USA'


        #TX----------------------
        if ('texas' in location) or ('TX' in Location): 
            loc_dict['state'] = 'TX'
            loc_dict['country'] = 'USA'
        if 'houston' in location: 
            loc_dict['city'] = 'Houston'            
            loc_dict['state'] = 'TX'
            loc_dict['country'] = 'USA'
        if 'dallas' in location: 
            loc_dict['city'] = 'Dallas'            
            loc_dict['state'] = 'TX'
            loc_dict['country'] = 'USA'
        if 'austin' in location: 
            loc_dict['city'] = 'Austin'            
            loc_dict['state'] = 'TX'
            loc_dict['country'] = 'USA'


        #UT------------------------
        if ('utah' in location) or ('UT' in Location):
            loc_dict['state'] = 'UT'
            loc_dict['country'] = 'USA'

        if 'salt lake city' in location:
            loc_dict['city'] = 'Salt Lake City'
            loc_dict['state'] = 'UT'
            loc_dict['country'] = 'USA'
        if ('salt lake' or 'slc ut' or 'sl utah') in location:
            loc_dict['city'] = 'Salt Lake City'
            loc_dict['state'] = 'UT'
            loc_dict['country'] = 'USA'
        if 'slc' == location:
            loc_dict['city'] = 'Salt Lake City'
            loc_dict['state'] = 'UT'
            loc_dict['country'] = 'USA'
        if 'park city' in location:
            loc_dict['city'] = 'Park City'
            loc_dict['state'] = 'UT'
            loc_dict['country'] = 'USA'
        if 'ogden' in location:
            loc_dict['city'] = 'Park City'
            loc_dict['state'] = 'UT'
            loc_dict['country'] = 'USA'


        #VA------------------------
        if ('virginia' in location) or ('va' == location) or ('VA' in Location): 
            loc_dict['state'] = 'VA'
            loc_dict['country'] = 'USA' 

        if 'arlington' in location:
            loc_dict['city'] = 'Arlington'            
            loc_dict['state'] = 'VA'
            loc_dict['country'] = 'USA' 
        if 'alexandria' in location:
            loc_dict['city'] = 'Alexandria'            
            loc_dict['state'] = 'VA'
            loc_dict['country'] = 'USA' 


        #VT-----------------------
        if ('vermont' in location) or (('vt') == location) or ('VT' in Location):
            loc_dict['state'] = 'VT'
            loc_dict['country'] = 'USA'
    
        if ('burlington') in location:
            loc_dict['city'] = 'Burlington'
            loc_dict['state'] = 'VT'
            loc_dict['country'] = 'USA'
        if ('stowe') in location:
            loc_dict['city'] = 'Stowe'
            loc_dict['state'] = 'VT'
            loc_dict['country'] = 'USA'
        if ('waterbury') in location:
            loc_dict['city'] = 'Waterbury'
            loc_dict['state'] = 'VT'
            loc_dict['country'] = 'USA'


        #WA-------------------------
        if ('location' == 'Washington') or ('WA' in Location): 
            loc_dict['state'] = 'WA'
            loc_dict['country'] = 'USA'

        if 'spokane' in location: 
            loc_dict['city'] = 'Spokane'
            loc_dict['state'] = 'WA'
            loc_dict['country'] = 'USA'
        if 'seattle' in location: 
            loc_dict['city'] = 'Seattle'
            loc_dict['state'] = 'WA'
            loc_dict['country'] = 'USA'
        if 'vancouver wa' in location: 
            loc_dict['city'] = 'Vancouver'
            loc_dict['state'] = 'WA'
            loc_dict['country'] = 'USA'
        

        #WV
        if ('west virginia' in location) or ('WV' in Location):
            loc_dict['state'] = 'WV'
            loc_dict['country'] = 'USA'


        #WY---------------------------
        if ('wyoming' in location) or ('wy' == location) or ('WY' in Location): 
            loc_dict['state'] = 'WY'
            loc_dict['country'] = 'USA'
        
        if 'jackson hole' in location: 
            loc_dict['city'] = 'Jackson'
            loc_dict['state'] = 'WY'
            loc_dict['country'] = 'USA'
        if 'jackson wy' in location: 
            loc_dict['city'] = 'Jackson'
            loc_dict['state'] = 'WY'
            loc_dict['country'] = 'USA'
        


    #Canada----------------------------------------
        if ('canada' in location): 
            loc_dict['country'] = 'CAN'

        #QC-------------
        if (('québec' or 'quebec')) in location or ('QC' in Location): 
            loc_dict['state'] = 'QC'
            loc_dict['country'] = 'CAN'

        if ('québec city' or 'quebec city') in location: 
            loc_dict['city'] = 'Québec City'
            loc_dict['state'] = 'QC'
            loc_dict['country'] = 'CAN'

        #BC-----------------
        if ('british columbia' in location) or ('BC' in Location): 
            loc_dict['state'] = 'BC'
            loc_dict['country'] = 'CAN'

        if ('vancouver ca' or 'vancouver bc' or 'vancouver canada' or 'vancouver british columbia') in location: 
            loc_dict['city'] = 'Vancouver'
            loc_dict['state'] = 'BC'
            loc_dict['country'] = 'CAN'
        if ('whistler') in location: 
            loc_dict['city'] = 'Whistler'
            loc_dict['state'] = 'BC'
            loc_dict['country'] = 'CAN'
        if ('revelstoke') in location: 
            loc_dict['city'] = 'Revelstoke'
            loc_dict['state'] = 'BC'
            loc_dict['country'] = 'CAN'
        if ('squamish') in location: 
            loc_dict['city'] = 'Squamish'
            loc_dict['state'] = 'BC'
            loc_dict['country'] = 'CAN'


        #AB------------------
        if ('alberta' in location) or ('AB' in Location): 
            loc_dict['state'] = 'AB'
            loc_dict['country'] = 'CAN'

        if ('calgary') in location: 
            loc_dict['city'] = 'Calgary'
            loc_dict['state'] = 'AB'
            loc_dict['country'] = 'CAN'
        if ('canmore alberta' or 'canmore ca' or 'canmore ab') in location: 
            loc_dict['city'] = 'Canmore'
            loc_dict['state'] = 'AB'
            loc_dict['country'] = 'CAN'

        #ON----------------------
        if ('ontario' in location) or ('ON' in Location): 
            loc_dict['state'] = 'ON'
            loc_dict['country'] = 'CAN'

        if 'toronto' in location: 
            loc_dict['city'] = 'Toronto'
            loc_dict['state'] = 'ON'
            loc_dict['country'] = 'CAN'
        

        
    #-----------------------------------------------        
    #International cities
        
        #Argentina-----------------
        if ('argentina') in location:
            loc_dict['country'] = 'ARG'

        if 'buenos aires' in location:
            loc_dict['city'] = 'Buenos Aires'
            loc_dict['country'] = 'ARG'


        #Australia------------------
        if 'australia' in location:
            loc_dict['country'] = 'AUS'     

        if 'melbourne' in location:
            loc_dict['city'] = 'Melbourne'
            loc_dict['country'] = 'AUS'
        if 'sydney australia' in location:
            loc_dict['city'] = 'Sydney'
            loc_dict['country'] = 'AUS'


        #Austria---------------
        if 'austria' in location: 
            loc_dict['country'] = 'AUT'

        if 'vienna' in location:
            loc_dict['city'] = 'Vienna'
            loc_dict['country'] = 'AUT'


        #Belgium-----------------
        if 'brussels' in location: 
            loc_dict['city'] = 'Brussels'
            loc_dict['country'] = 'BEL'
        if 'belgium' in location: 
            loc_dict['country'] = 'BEL'

        if 'singapore' in location: 
            loc_dict['city'] = 'Singapore'
            loc_dict['country'] = 'SGP'


        #Colombia------------------
        if ('colombia') in location: 
            loc_dict['country'] = 'COL'

        if ('bogota' or 'bogotá') in location: 
            loc_dict['city'] = 'Bogotá'
            loc_dict['country'] = 'COL'


        #China------------------
        if ('china') in location:
            loc_dict['country'] = 'CHN'

        if 'beijing' in location:
            loc_dict['city'] = 'Beijing'
            loc_dict['country'] = 'CHN'
        if 'shanghai' in location: 
            loc_dict['city'] = 'Shanghai'
            loc_dict['country'] = 'CHN'


        #Denmark-------------------------
        if ('denmark' or 'danmark') in location:
            loc_dict['country'] = 'DNK'
        
        if ('copenhagen' or 'københavn' or 'danmark') in location:
            loc_dict['city'] = 'Copenhagen'
            loc_dict['country'] = 'DNK'
        

        #Ethiopia-----------------
        if 'ethiopia' in location:
            loc_dict['country'] = 'ETH'


        #France-------------------
        if 'france' in location:
            loc_dict['country'] = 'FRA'

        if 'chamonix' in location:
            loc_dict['city'] = 'Chamonix'
            loc_dict['country'] = 'FRA'


        #Germany-----------------------
        if ('germany' or 'deutschland') in location: 
            loc_dict['country'] = 'DEU'
        if 'berlin' in location:
            loc_dict['city'] = 'Berlin'
            loc_dict['country'] = 'DEU'


        #Hong Kong----------------
        if 'hong kong' in location:
            loc_dict['city'] = 'Hong Kong'
            loc_dict['country'] = 'HKG'


        #India-------------------
        if 'new delhi' in location: 
            loc_dict['city'] = 'New Delhi'
            loc_dict['country'] = 'IND'
        if 'india' in location:
            loc_dict['country'] = 'IND'
        if 'mumbai' in location: 
            loc_dict['city'] = 'Mumbai'
            loc_dict['country'] = 'IND'


        #Kenya--------------------
        if 'nairobi' in location: 
            loc_dict['city'] = 'Nairobi'
            loc_dict['country'] = 'KEN'
        if 'kenya' in location: 
            loc_dict['country'] = 'KEN'


        #Lebanon-----------------
        if ('lebanon') == location:
            loc_dict['country'] = 'LBN'
        if 'لبنان' in location:
            loc_dict['country'] = 'LBN'

        if ('beirut' or 'beyrouth' or 'بيروت') in location:
            loc_dict['city'] = 'Beirut'
            loc_dict['country'] = 'LBY'


        #Libya-----------------
        if 'libya' in location:
            loc_dict['country'] = 'LBY'

        

        #Mexico-----------------------------
        if ('méxico' or 'mexico') in location:
            loc_dict['city'] = ''
            loc_dict['state'] = ''
            loc_dict['country'] = 'MEX'

        if ('mexico city' or 'ciudad de mexico' or 'ciudad de méxico') in location:
            loc_dict['city'] = 'Mexico City'
            loc_dict['country'] = 'MEX'
        if 'monterrey nuevo león' in location:
            loc_dict['city'] = 'Monterrey'
            loc_dict['country'] = 'MEX'

        
        
        #Netherlands-----------------
        if ('netherlands') in location: 
            loc_dict['country'] = 'NLD'

        if ('amsterdam') in location: 
            loc_dict['city'] = 'Amsterdam'
            loc_dict['country'] = 'NLD'


        #New Zealand-----------------
        if ('new zealand' in location) or ('NZ' in Location): 
            loc_dict['country'] = 'NZL'

        if ('aukland') in location: 
            loc_dict['city'] = 'Aukland'
            loc_dict['country'] = 'NLD'
        

        #Nigeria----------------
        if 'nigeria' in location: 
            loc_dict['country'] = 'NGA'

        
        #Pakistan------------------
        if 'pakistan' in location: 
            loc_dict['country'] = 'PAK'
            
        if 'islamabad' in location: 
            loc_dict['city'] = 'Islamabad'
            loc_dict['country'] = 'PAK'
        if 'karachi' in location: 
            loc_dict['city'] = 'Karachi'
            loc_dict['country'] = 'PAK'
        if 'sialkot' in location: 
            loc_dict['city'] = 'Sialkot'
            loc_dict['country'] = 'PAK'

            
        #South Korea----------------
        if 'south korea' in location:
            loc_dict['country'] = 'KOR'

        if 'seoul' in location:
            loc_dict['city'] = 'Seoul'
            loc_dict['country'] = 'KOR'
        

        #Sweden----------------
        if 'sweden' in location:
            loc_dict['country'] = 'SWE'   
        

        #Switzerland-----------------
        if 'switzerland' in location: 
            loc_dict['country'] = 'CHE'

        if 'geneva' in location: 
            loc_dict['city'] = 'Geneva'
            loc_dict['country'] = 'CHE'
        if 'zermatt' in location: 
            loc_dict['city'] = 'Zermatt'
            loc_dict['country'] = 'CHE'
        if 'zurich' in location: 
            loc_dict['city'] = 'Zurich'
            loc_dict['country'] = 'CHE'


        #Taiwain----------------
        if 'taiwan' in location: 
            loc_dict['city'] = 'Taiwan'
            loc_dict['country'] = 'TWN'


        #Turkey-------------------------
        if ('turkey' or 'türkiye') in location:
            loc_dict['country'] = 'TUR'

        if 'istanbul' in location:
            loc_dict['city'] = 'Istanbul'
            loc_dict['country'] = 'TUR'


        #Ukraine-----------------
        if ('ukraine' or 'Україна' or 'Ukraïna') in location:
            loc_dict['city'] = 'Kyiv'
            loc_dict['country'] = 'UKR'

        if ('kyiv' or 'kiev' or 'Київ') in location:
            loc_dict['country'] = 'UKR'


        #United Arab Emirates-----------
        if ('united arab emirates' or 'الإمارات العربية المتحدة') in location:
            loc_dict['country'] = 'ARE'
            
        if 'dubai' in location:
            loc_dict['city'] = 'Dubai'
            loc_dict['country'] = 'ARE'


        #United Kingdom--------------
        if (('united kingdom' or 'scotland' or 'northern ireland') in location) or ('england' == location) or ('uk' == location) or ('UK' in Location):
            loc_dict['country'] = 'GBR'
        
        if 'london' in location:
            loc_dict['city'] = 'London'
            loc_dict['country'] = 'GBR'
        
    
    location_iterator(user_location)

    #print(loc_dict)
    return loc_dict

#parse_location('I live in Washington DC')