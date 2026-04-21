class Animal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def __print__(self):
        print(f'Arm Length: {self.arm_length}')
        print(f'Leg Length: {self.leg_length}')
        print(f'Number of Eyes: {self.num_eyes}')
        print(f'Has a Tail: {self.has_tail}')
        print(f'Has Fur: {self.is_furry}')
