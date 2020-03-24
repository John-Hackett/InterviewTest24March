class EdifactParser():
    default_una = ":+.? '"

    def __init__(self, message):
        self.una = None
        self.edifact_message = self.parseMessage(message)

        if (self.edifact_message != False):
            self.loc_segments = self.returnLocSegments()
        else:
            self.una = EdifactParser.default_una
            self.loc_segments = []

        self.sec_third_segments = self.getSegments()


    def parseMessage(self,message):
        """
        Attempt to open a file, find its UNA code and return the message in an array

        """
        try:
            with open(message, 'r') as edifact:
                content = edifact.read()
                content = self.findUna(content)
                return content
    # Do something with the file
        except IOError:
            print("File not accessible")
            return False
        except Exception:
            print("Something went wrong")
            return False

    def findUna(self,firstLine):
        """
        Generates an una from the file or from a default value, then splits the full message into an array based on the una code

        """
        una_present = False
        if (len(firstLine)>=3):
            una_present = True if firstLine[:3] == "UNA" else False
        if (len(firstLine)>=10):
            self.una = firstLine[3:10] if una_present else False
        else:
            self.una = EdifactParser.default_una
        if una_present:
            firstLine = firstLine[10:]
        # Need to identify special characters in text
        firstLine = self.splitMessage(firstLine)
        return firstLine

    def splitMessage(self,message):
        """
        Searches for the special char and changes the next character if it is equal to the terminating character. Then splits the message on the terminating char and then changes all chars back

        """
        releaseChar = self.una[3]
        parsed_message = message.split(self.una[len(self.una)-1])
        parsed_message = [parsed_message[x] + parsed_message[x+1] if parsed_message[x][-2] == releaseChar else parsed_message[x] for x in range(len(parsed_message[:-1]))]
        return parsed_message


    def returnLocSegments(self):
        """
        Looks for LOC as the first three letters of each element.

        """
        loc_segments = [x for x in self.edifact_message if x[:3] == "LOC"]
        return loc_segments

    def getSegments(self):
        """
        This function creates an array of the second and third elements per loc segments based on the una provided

        """
        releaseChar = self.una[3]
        segments = [[y for y in x.split(self.una[1])] for x in self.loc_segments]
        for x in segments:
            x.pop(0)
            for y in range(len(x)):
                if (x[y][-1] == releaseChar):
                    x[y] = x[y] + x[y+1]
        results = []
        def answer(item,results):
            results += item[:2]

        [answer(z,results) for z in segments]
        return results
