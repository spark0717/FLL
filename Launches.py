#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Key a (path):
#
#  1 - angle
#  2 - turn radius
#  3 - motor id

# Key b (speed):
#
#  1 - cm/sec
#  2 - deg/sec
#  3 - rot/sec

# Key c (target):
#
#  1 - drive centimeters
#  2 - target centimeters
#  3 - target degrees
#  4 - seconds

#   ["MoveType"        ,  a  ,  b  ,  c  ],
#
# LaunchName = [
#   ["Drive"           ,  1  ,  1  ,  1  ],
#   ["DriveUltrasonic" ,  1  ,  1  ,  2  ],
#   ["Turn"            ,  2  ,  2  ,  3  ],
#   ["LineFollow"      ,        1        ],
#   ["MotorOn"         ,  3  ,  3        ],
#   ["MotorOff"        ,  3              ],
#   ["Wait"            ,              4  ],
# ]

# Run #1- Bench (M04) and Slide (M03)
East = [
    # Does Bench 
    ["Drive"            ,  0  ,  40  ,  45  ],
    ["MotorOn"          ,  0  , -8          ],
    ["MotorOff"         ,  0                ],
    # Turns and faces Slide
    ["Drive"            ,  0  , -25   , -45 ],
    ["Turn"             ,  0  ,  45   ,  90 ],
    ["Drive"            ,  0  ,  40   ,  45 ],
    # Code if we are NOT using a passive attachment:
    # ["MotorOn"       ,   0  ,  -4    ], 
    # ["MotorOff"      ,   0           ],
    ["Wait"             ,                 4 ],
    ["Drive"            ,  0  , -40   , -40 ],
    # Comes back to home
    ["Turn"             ,  0  , -30   ,  30 ],
    ["Drive"            ,  0  , -40   , -40 ],
   
]


# Run #2- Step Counter (M02), Pull-up Bar (M06), Boccia (M08), Basketball (M05)
NorthEast = [
    ["Drive"           ,  0  ,  50  ,  25  ],
    ["Drive"           ,  0  ,  20  ,  10  ],
    ["Drive"           ,  0  ,  -20 ,  -10 ],
    ["Turn"            ,  25 ,  -30 ,  -30 ],
    ["Drive"           ,  0  ,  30  ,   15 ],
    ["Turn"            ,  25 ,  30  ,   15 ],
    ["Drive"           ,  0  ,  60  ,   35 ],
]

# NOT UPDATED YET
# Run #3- Treadmill (M11), Row machine (M12), Weight machine (M13), Cell phone (M10)
NorthWest = [
    #Starts turning the motors to lock the towers in place
    ["MotorOn"         ,  0  , -4          ],
    ["Wait"            , 0.80              ],
    ["MotorOff"        ,  0                ],
    ["MotorOn"         ,  1  ,  4          ],
    ["Wait"            , 0.17              ],
    ["MotorOff"        ,  1                ],
    #Turns towrds traffic jam
    ["Turn"            , 11  ,  30  ,  90  ],
    #Drives until it has wedged under the traffic jam
    ["DriveUltrasonic" ,  90 ,  20  ,  120 ],
    #Fully lifts up traffic jam
    ["Turn"            , 10  , -30  ,   0  ],
    #Goes forward and turns towrds tan towers
    ["Drive"           ,  0  ,  20  ,  10  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["DriveUltrasonic" ,  90 ,  20  ,  149 ],
    ["Turn"            ,  0.9, -30  ,  0   ],
    ["DriveUltrasonic" ,  0  ,  20  ,  50  ],
    #Drops of tan towers
    ["MotorOn"         ,  0  ,  4          ],
    ["Wait"            , 0.80              ],
    ["MotorOff"        ,  0                ],
    #Backs up and turns towrds red towers
    ["DriveUltrasonic" ,  0  , -20  ,  15  ],
    ["Turn"            ,  0  ,  30  ,  90  ],
    ["Drive"           , 90  , -20  , -30  ],
    #Drops of red towers
    ["MotorOn"         ,  1  , -4          ],
    ["Wait"            , 0.17              ],
    ["MotorOff"        ,  1                ],
    ["Wait"            ,  1                ],
    #Comes back home
    ["Drive"           ,  90 , -20  , -50  ],
    #Closes the door to fit in base
    ["MotorOn"         ,  1  ,  0.01       ],
    ["Drive"           ,  90 , -20  , -65  ],
]

#Run #4- Tire Flip (M09), Robot dance (M07)
RobotDance = [
    
]

Launches = [East, NorthEast, NorthWest, RobotDance]
