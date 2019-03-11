"""
A   Baby   class and functions that use/test it.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jairyq Underwood.
"""  # Done : 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """
    After you have made the Baby class, run this module. If your Baby
    class is correct, the output of the code below should be exactly this:

        Hello baby McKinley!
        Hello baby Keegan!
        - - - - -
        Baby Keegan is sleeping.
        Thank you for feeding baby McKinley.
        Baby McKinley is sleeping.
        Baby McKinley is awake.  Time for food.
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        - - - - -
        Baby Keegan is awake.  Time for food.
        Thank you for feeding baby McKinley.
        Baby McKinley is sleeping.
        Baby McKinley is awake.  Time for food.
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
    """
    mckinley = Baby('McKinley')
    keegan = Baby('Keegan')

    for k in range(2):
        print('- - - - -')
        keegan.hour_passes()
        mckinley.feed_baby()

        for j in range(4):
            mckinley.hour_passes()


###############################################################################
# TODO: 2.
#
#  Step 2a:  Implement a class called   Baby   that has a constructor method
#            (__init__) and two other methods, as described below.
#
#  Step 2b:  Test your finished   Baby   class by running this module.
#            Your code passes the test if it displays exactly the output
#            shown in the doc_string for main.
#
# -----------------------------------------------------------------------------
# Here (below) are the methods that you must implement in your Baby class:
# -----------------------------------------------------------------------------
#
# Constructor method (__init__)
#     What comes in:
#        -- self
#        -- a string for the name of the baby
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Sets instance variables as needed [YOU FIGURE OUT WHAT IS NEEDED!]
#        -- Prints 'Hello baby <your baby's name>!'
#     Example:
#         b = Baby('McKinley')   causes the following to be printed:
#               Hello baby McKinley!
#
# feed_baby
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Prints 'Thank you for feeding baby <your baby's name>.'
#        -- Modifies instance variables as needed
#     Example:
#         b = Baby('Joshua')
#         b.feed_baby()         causes the following to be printed:
#               Hello baby Joshua!
#               Thank you for feeding baby Joshua.
#
# hour_passes
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#      -- If this is the FIRST time this method has been called
#         since this Baby was created or last fed, then this method prints:
# 	             'Baby <your baby's name> is sleeping.'
#
#      -- If this is the SECOND time this method has been called
#         since baby was created or last fed, then this method prints:
# 	             'Baby <your baby's name> is awake.  Time for food.'
#
#      -- If this is the THIRD (OR MORE) time this method has been called
#           since baby was created or last fed, then this method prints:
#         'Baby <your baby's name> is CRYING uncontrollably!  Feed the Baby!'
#
###############################################################################

###############################################################################
# The   Baby   class (and its methods) should begins here.
# Here is a reminder for the syntax to create a new class.
#
#      class NameOfClass(object):
#          """ Brief description of what an object of the class 'is'. """
#
###############################################################################
class Baby(object):
    def __init__(self, baby_name):
        self.baby_name = baby_name
        print('Hello baby ' + baby_name)
        self.count_time = 0
        self.count_food = 0

    def feed_baby(self):
        baby = self.baby_name
        self.count_food = self.count_food + 1
        print('Thank you for feeding ' + baby)

    def hour_passes(self):
        if self.count_food == 1:
            self.count_time = 0
            self.count_food = 0
        baby = self.baby_name
        self.count_time = self.count_time + 1
        if self.count_time == 1 or self.count_food == 1:
            print('Baby ' + baby + ' is sleeping.')
        if self.count_time == 2 or self.count_food == 2:
            print('Baby ' + baby + ' is awake. Time for food.')
        if self.count_time >= 3 or self.count_food >= 3:
            print('Baby ' + baby + ' is CRYING Uncontrollably! Feed the Baby!')





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
