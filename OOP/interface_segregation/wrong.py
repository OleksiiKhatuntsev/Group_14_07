from abc import ABCMeta, abstractmethod

# Interface Substitution Principle
# No client should be forced to depend on methods it does not use
'''
A larger interface bundled with all methods makes it mandatory for all classes to provide implementation of all the methods even if 
some methods are not relevant to them
'''

class CommunicationDevice():
  @abstractmethod
  def make_calls(self):
    pass

  @abstractmethod
  def send_sms(self):
    pass

  @abstractmethod
  def browse_internet(self):
    pass

class SmartPhone(CommunicationDevice):
  def make_calls(self):
    #implementation
    pass

  def send_sms(self):
    #implementation
    pass

  def browse_internet(self):
    #implementation
    pass

  class LandlinePhone(CommunicationDevice):
    def make_calls(self):
      #implementation
      pass

    def send_sms(self):
      raise Exception("Landline phone cannotn send sms")
      pass

    def browse_internet(self):
      #just pass or raise exception as this feature is not supported
      pass