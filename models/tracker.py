class Tracker:

  iteration_no = 0
  total_iteration = 0

  def __init__(self):
    pass

  @staticmethod
  def get_iteration_no():
    return Tracker.iteration_no

  @staticmethod
  def get_total_iterations():
    return Tracker.total_iteration
  
  @staticmethod
  def perform_step():
    Tracker.iteration_no += 1
  
  @staticmethod
  def reset_iteration_counter():
    Tracker.iteration_no = 0
  
  @staticmethod
  def set_total_iteration(number):
    Tracker.total_iteration = number