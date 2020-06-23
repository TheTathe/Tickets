from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)


@acts_as_state_machine
class TicketState:
    arrived = State(initial=True)
    waiting = State()
    running = State()
    stopped = State()

    wait = Event(from_states=(arrived, running, stopped), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    stop = Event(from_states=(running, waiting, arrived), to_state=stopped)

    def __init__(self, name):
        self.name = name

    @after('wait')
    def wait_info(self):
        print(f'{self.name}  IS WAITING')

    @after('run')
    def run_info(self):
        print(f'{self.name}  RUNNINGUJE')

    @after('terminate')
    def block_info(self):
        print(f'{self.name}  TERMINATORUJE')


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as err:
        print(f'Error: TRANZYCJA JEBLA  {process.name} Z {process.current_state} DO {event_name} NIESTETY')


def state_info(process):
    print(f'STAN PROCESA {process.name}: {process.current_state}')

def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    STOPPED = 'stopped'

    p1, p2 = TicketState('ticket1'), TicketState('ticket2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.stop, STOPPED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.stop, STOPPED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]


if __name__ == '__main__':
    main()