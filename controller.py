"""
    Quadcopter Simulator
    --
    A quick way to test stabilzation algorithms.
    
    John Drogo
    Septemer 15, 2014
    
    YOU NEED TO USE THIS IN BLENDER!
    Look for spots that say CHANGE THIS and modify them as needed.
    
    This simulator does not take aerodynamics or pressure into account.
    
    The red marks on the quadcopter mark its front,
    each fan is numbered clockwise with fan 0 being the front left.
    
    ALL UNITS ARE IN SI!
    (Angles are in radians.)
    
    When using the acceleration or velocity lists index 0 indicates the x axis,
    1 is the y, and 2 is the z.
    
    I consider clockwise a positive RPM, and counterclockwise as negative.

    Happy flying!

"""

import bge
import random
import math

class QuadRotor:
  def __init__(mass = 1):
    self.p_m = .018 #Propellor mass.
    self.p_r = .10  #Prop length.
    q_m = own.mass #Mass of quadcopter (set using the physics tab below.
    q_r = .15 #Distance from prop center to quad center of mass.

  def desiredVelocity():
  def desiredAcceleration():
  def rotorVelocities():
  def calculateAccel():
