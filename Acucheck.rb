puts "Enter number of rooms"
number_rooms = gets.to_i
acuity_hash = Hash.new
count = 0
while count < number_rooms
  puts "Input patient room number"
  room = gets.to_i
  #Lists and puts(s/input for Procedural acuity
  puts "1- No Procedures"
  puts "2- IV Starts, Foley Catheter"
  puts "3- Vitals, Neuro Check, Bladder Scans"
  puts "4- Bedside Procedure, Physician post-op, frequent catheterization"
  puts "Input Procedural Acuity 1-4"
  procedural = gets.to_i

  #Lists and puts(s/input for Nutritional acuity
  puts "1- Setup Self"
  puts "2- Ordering Assistance"
  puts "3- Feed"
  puts "4- Tubefeed, Aspiration Procedures"
  puts "Input Nutritional Acuity 1-4 "
  nutritional = gets.to_i
		
  #Lists and puts(s/input for Medication acuity
  puts "Input Medication Acuity 1-4 "
  puts "1- Minimal Oral"
  puts "2- Moderate PO/IV"
  puts "3- Dysphasia/Multi IV"
  puts "4- Chemo/GTUBE/Complex IV"
  medication = gets.to_i

  #Lists and puts(s/input for Mobility acuity
  puts "Input Mobility Acuity 1-4 "
  puts "1- Ad lib"
  puts "2- Assist of SB"
  puts "3- Assist of 1"
  puts "4- Assist of 2"
  mobility = gets.to_i

  #Lists and puts(s/inputs for Behavioral Acuity
  "Input Behavioral Acuity 1-4"
  puts "1- Calls Appropriately/No Needs"
  puts "2- Some Education/ Calls Often"
  puts "3- Anxious/ Calls Frequently"
  puts "4- New Diagnosis, Calls very frequently, highly anxious"
  behavioral= gets.to_i


  acuity = procedural + nutritional + medication + mobility + behavioral
  puts "Patient in room #{room}, is graded at an acuity of #{acuity}"

  
  acuity_hash[room] = acuity
  puts acuity_hash
  count = count + 1
  
end