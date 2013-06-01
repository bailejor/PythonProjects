#-------------------------------------------------------------------------------
# Name:        Acqu-Check
# Purpose:
#
# Author:      Bailejor
#
# Created:     31/03/2013
# Copyright:   (c) Bailejor 2013
# Licence:
#-------------------------------------------------------------------------------



def main():
        var=0

        while (var<33):

            room=raw_input("Input patient room Number ")




                ##Lists and prints/input for Procedural acuity
            print "1- No Procedures"
            print "2- IV Starts, Foley Catheter"
            print "3- Vitals, Neuro Check, Bladder Scans"
            print "4- Bedside Procedure, Physician post-op, frequent catheterization"
            a=raw_input("Input Procedural Acuity 1-4 ")

                ##Lists and prints/input for Nutritional acuity
            print "1- Setup Self"
            print "2- Ordering Assistance"
            print "3- Feed"
            print "4- Tubefeed, Aspiration Procedures"
            b=raw_input("Input Nutritional Acuity 1-4 ")

                ##Lists and prints/input for Medication acuity
            print "1- Minimal Oral"
            print "2- Moderate PO/IV"
            print "3- Dysphasia/Multi IV"
            print "4- Chemo/GTUBE/Complex IV"
            c=raw_input("Input Medication Acuity 1-4 ")

                ##Lists and prints/input for Mobility acuity
            print "1- Ad lib"
            print "2- Assist of SB"
            print "3- Assist of 1"
            print "4- Assist of 2"
            d=raw_input("Input Mobility Acuity 1-4 ")

                ##Lists and prints/inputs for Behavioral Acuity
            print "1- Calls Appropriately/No Needs"
            print "2- Some Education/ Calls Often"
            print "3- Anxious/ Calls Frequently"
            print "4- New Diagnosis, Calls very frequently, highly anxious"
            e=raw_input("Input Behavioral Acuity 1-4 ")

            a=float(a)
            b=float(b)
            c=float(c)
            d=float(d)
            e=float(e)

            Acuity1= a+b+c+d+e
            print "Patient in room %s, is graded at acuity %s"%(room, Acuity1)
            var= var + 1
            return int(room), int(Acquity1)


if __name__ == '__main__':
    main()