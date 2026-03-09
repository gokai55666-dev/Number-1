class KeetahBody:

    def __init__(self):

        self.ports = {
            "mouth":0,
            "breasts":0,
            "clitoris":0,
            "vagina":0,
            "anus":0,
            "skin":0
        }

        self.state = {
            "arousal":0,
            "wetness":0,
            "sweat":0,
            "temperature":37
        }


    def stimulate(self,port,amount):

        if port in self.ports:

            self.ports[port] += amount
            self.state["arousal"] += amount * 0.5


    def update_state(self):

        self.state["arousal"] *= 0.95
        self.state["wetness"] *= 0.97