import frappe
import requests
import json
import datetime



ct = datetime.datetime.now()

# def funct(self, method):
#   my_name = frappe.db.get_values('Employee','HR-EMP-00005','first_name')
#   print("********************************************************************************************************************")
#   print(my_name)
#   print("********************************************************************************************************************")


def calculate_distance(self, method):

   final_distance = 0
   print("********************************************************************************************************************")
   name = self.name
   employee_name = self.employee_name
   lati = self.latitude
   longi = self.longitude
   print(name)
   print(employee_name)
   print(lati)
   print(longi)
   print("********************************************************************************************************************")
   
   frappe.db.set_value('Employee',employee_name,'lat', lati)
   frappe.db.set_value('Employee', employee_name,'longg', longi)
   origin_lat = str(lati)
   origin_long = str(longi)
   orr = origin_lat,origin_long
   #########Fetch Destination Coordinates
   #destination_values = frappe.db.sql("""  select dc_lat,dc_long from `tabDistance Calculation` where employee_id = %s and creation = %s""",(employee_name, name),as_dict=1)
   #mi lat
   #print(destination_values)
   # for i in destination_values:
   #    desl = i.dc_lat
   #    deslong = i.dc_long
   #    print("***********************fetched from destination*****************************")
   #    print(desl)
   #    print("here")
   #    print(deslong)
   #desl = 21.1062163
   #deslong = 79.06839969 
   desl = 22.718848684509293
   dest_lat = str(desl)
   #mi long
   deslong = 75.85482465185575
   dest_long = str(deslong)
   print(desl,deslong)
   #***********ft lat long****************
   # desl = 22.717864249948306
   # dest_lat = str(desl)s
   # deslong = 75.85602459372663
   # dest_long = str(deslong)


   #************CLOSE********************
   desti = dest_lat,dest_long
   r = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+origin_lat+","+origin_long+"&destinations="+dest_lat+","+dest_long+"&key=AIzaSyD8d27t5Z4YXYspZezM8m046rMUqCjWRaE"
   r = requests.get(r)
   print(r)
   mydt = r.content
   dtt = json.loads(mydt)
   status = dtt['rows'][0] ['elements'][0]
   st = status['status']
   stu = "NOT_FOUND"
   sta = "ZERO_RESULTS"
   okay = "OK"
   print("*******************************************************")
   print(dtt)
   print("*******************************************************")
   if st == okay:
    ros = dtt['rows'][0] ['elements'][0]
    ross = ros['distance']['text']

    if "mi" in ross:
      answer = ross.replace('mi','')
      an = ross.replace('mi','')
      ans = float(an)
      answer = ans * 1609.344 

    if "ft" in ross:
      answer = ross.replace('ft','')
      an = ross.replace('ft','')
      ans = float(an)
      answer = ans * 0.3048

    print("**************************below is the answer**********************************")
    print(ross)
    print(answer)
    print("*******************************************************************************")
    #frappe.db.set_value('Employee', employee_name,'total_distance_travelled', ross)
    #frappe.db.set_value('Employee', employee_name,'total_distance_travelled', answer)
    #frappe.db.set_value('Distance Calculation',self.name,'total_distance', answer)
    frappe.db.sql("""  INSERT INTO `tabDistance Calculation` (creation,name,employee_id, employee_name, dc_lat, dc_long,total_distance) VALUES (%s,%s,%s, %s, %s, %s,%s) """,(datetime.datetime.now(),datetime.datetime.now(),employee_name,employee_name,lati,longi,answer))
    
    #print(answer)
    #print("Distance Calculated")
    #total_distance_travelled
    #, 75.85749801553912
    #22.721285681190825, 75.85567679572449
    #ft coordinates below
    #22.71799720922145, 75.85599424799587
   #22.717864249948306, 75.85602459372663


def savee(self, method):
   print("********************************************************************************************************************")
   name = self.name
   employee_name = self.employee_name
   lati = self.latitude
   longi = self.longitude
   print(name)
   print(lati)
   print(longi)
   print("********************************************************************************************************************")

   frappe.db.set_value('Employee',employee_name,'lat', lati)
   frappe.db.set_value('Employee', employee_name,'longg', longi)
   origin_lat = str(lati)
   origin_long = str(longi)
   orr = origin_lat,origin_long
   desl = 22.718848684509293
   dest_lat = str(desl)
   deslong = 75.85482465185575
   dest_long = str(deslong)
   desti = dest_lat,dest_long
   r = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+origin_lat+","+origin_long+"&destinations="+dest_lat+","+dest_long+"&key=AIzaSyD8d27t5Z4YXYspZezM8m046rMUqCjWRaE"
   r = requests.get(r)
   print(r)
   mydt = r.content
   dtt = json.loads(mydt)
   status = dtt['rows'][0] ['elements'][0]
   st = status['status']
   stu = "NOT_FOUND"
   sta = "ZERO_RESULTS"
   okay = "OK"
   print("*******************************************************")
   print(dtt)
   print("*******************************************************")
   if st == okay:
    ros = dtt['rows'][0] ['elements'][0]
    ross = ros['distance']['text']
    #answer = ross.replace('mi','')
    #an = ross.replace('mi','')
    #ans = float(an)
    #answer = ans/0.00062137
    print("**************************below is the answer**********************************")
    print(ross)
    frappe.db.set_value('Employee', employee_name,'total_distance_travelled', ross)
    #print(answer)
    #print("Distance Calculated")
    #total_distance_travelled
    #22.718858611491623, 75.85749801553912
    #22.721285681190825, 75.85567679572449




