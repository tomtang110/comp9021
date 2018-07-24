# Written by Eric Martin for COMP9021


from numpy.random import poisson, exponential

'''
Illustrates the use of the queue ADT in modeling a real queue.

Prompts the user to input:
- the average time, lambda, between two successive arrivals of customers joining the queue,
  in minutes;
- the average time, mu, needed to serve a customer when her turn comes, in minutes;
- how long the simulation should be run, in hours.

It is assumed that the inter-arrival time between successive customers and the service time
for a given customer are modeled by an exponentially distributed random variables with
an expected value of lambda and mu, respectively.

The first two inputs allow one to theoretically estimate:
- the average number of customers in the queue including those being served;
- the average number of customers in the queue waiting to be served;
- the average waiting time for a customer, excluding service time;
- the average waiting and service time for a customer.
These estimates are computed and displayed.

Then a simulation is run, with at every second, the following happening.
- Some customers possibly join the queue, their total number being randomly generated
  following a Poisson distribution with an expected value of lambda, based on the relationship
  the latter has with the exponential distribution with the same expected value.
- The requested service time of the customers who have just joined the queue, if any,
  is randomly generated following an exponential distribution with an expected value of mu,
  and rounded to an integral number of seconds.
- If somebody is being served but the remainig service time is 0, then that customer leaves
  the queue.
- Whether the previous case applies or nobody is being served, if the queue is not empty then the
  customer at the front of the queue starts being served. Her requested service time could be 0,
  in which case she would immediately quit the queue and the process would repeat with the next
  customer, if any; otherwise what remains of the service time for this customer is decreased by 1.
- Running sums of how long a customer had to wait before she could start being served, of how long
  it took a customer to wait and be fully served, and of how long the queue is after the customers
  who have just been served have left,including or not the customer now being served, if any, are
  kept. At the end of the simulation, these sums are divided by the number of seconds during which
  the simulation has been run to yield the empirical values of the entities that have previously
  been theoretically estimated.
  The total number of customers who have joined the queue is also displayed.
'''


from random import random
from math import log

import queue_adt




class Customer:
    def __init__(self, arrival_time = 0, service_time = 0):
        self.arrival_time = arrival_time
        self.service_time = service_time


class QueueSimulation:
    def __init__(self):
        self.average_time_between_two_arrivals = float(input('Enter the average time, in minutes, '
                                                                            'between two arrivals: '
                                                            )
                                                      ) * 60
        self.average_service_time = float(input('Enter the average time, in minutes, '
                                                                      'needed to serve a customer: '
                                               )
                                         ) * 60
    def display_time(self, time):
        hours, seconds = divmod(round(time), 3600)
        minutes, seconds = divmod(seconds, 60)
        no_time = True
        if hours:
            no_time = False
            print(f' {hours}', end = ' ')
            print('hours', end = '') if hours > 1 else print('hour', end = '')
        if minutes:
            no_time = False
            time_elapsed = True
            print(f' {minutes}', end = ' ')
            print('minutes', end = '') if minutes > 1 else print('minute', end = '')
        if seconds:
            no_time = False
            time_elapsed = True
            print(f' {seconds}', end = ' ')
            print('seconds', end = '') if seconds > 1 else print('second', end = '')
        print()
        if no_time:
            print('Instantaneous')

    def compute_and_display_estimates(self):
        traffic_intensity = self.average_service_time / self.average_time_between_two_arrivals
        average_nb_in_queue = traffic_intensity / (1 - traffic_intensity)
        average_nb_waiting_in_queue = average_nb_in_queue * traffic_intensity
        print('Estimated average number of customers in queue including those being served: '
                                                                  f'{round(average_nb_in_queue, 2)}'
             )
        print('Estimated average number of customers in queue waiting to be '
                                                  f'served: {round(average_nb_waiting_in_queue, 2)}'
             )
        print('Estimated average waiting time, including serving time:', end = '')
        self.display_time(average_nb_in_queue * self.average_time_between_two_arrivals)
        print('Estimated average waiting time, excluding serving time:', end = '')
        self.display_time(average_nb_waiting_in_queue * self.average_time_between_two_arrivals)
        print()

    def run_simulation(self):
        simulation_time = int(input('For how long, in hours, should the simulation be run? '))
        simulation_limit = simulation_time * 3600
        q = queue_adt.Queue()
        nb_of_customers = 0
        cumulative_queue_length = 0
        cumulative_waiting_length = 0
        # A service time of -1 indicates that nobody is being served, which can only happen
        # if the queue is empty, possibly following the departure of the last served customer.
        service_time = -1
        cumulative_waiting_time = 0
        cumulative_waiting_and_serving_time = 0
        for simulation_tick in range(simulation_limit):
            new_customers = poisson(1 / self.average_time_between_two_arrivals)
            nb_of_customers += new_customers
            for _ in range(new_customers):
                customer = Customer()
                customer.arrival_time = simulation_tick
                customer.service_time = round(exponential(self.average_service_time))
                q.enqueue(customer)
            # A new customer can now start being served.
            if service_time == -1 and not q.is_empty():
                service_time = q.peek_at_front().service_time
                cumulative_waiting_time += simulation_tick - q.peek_at_front().arrival_time
            # If the customer at the front has been served, then she should now quit the queue
            # and all customers that follow her and that need no time to be served should follow
            # her (these guys have been queuing for a while just to find out that they do not
            # have an indispensible piece of information when they are about to be served;
            # surely, they are pretty upset when they quit the queue).
            while service_time == 0:
                cumulative_waiting_and_serving_time += simulation_tick - q.dequeue().arrival_time
                if not q.is_empty():
                    service_time = q.peek_at_front().service_time
                    cumulative_waiting_time += simulation_tick - q.peek_at_front().arrival_time
                else:
                    service_time = -1
            cumulative_queue_length += len(q)
            if not q.is_empty():
                service_time -= 1
                cumulative_waiting_length += len(q) - 1
        if nb_of_customers:
            print(f'Number of customers who have joinded the queue: {round(nb_of_customers, 2)}')
            print('Average number of customers in queue including those being served: '
                                           f'{round(cumulative_queue_length / simulation_limit, 2)}'
                 )
            print('Average number of customers in queue waiting to be served: '
                                         f'{round(cumulative_waiting_length / simulation_limit, 2)}'
                 )
            print('Average waiting time, including serving time:', end = '')
            self.display_time(cumulative_waiting_and_serving_time / nb_of_customers)
            print('Average waiting time, excluding serving time:', end = '')
            self.display_time(cumulative_waiting_time / nb_of_customers)
        else:
            print('No one has joined the queue; a very quiet day...')

            
if __name__ == '__main__':
    simulation = QueueSimulation()
    simulation.compute_and_display_estimates()
    simulation.run_simulation()
