class EarlyStopper:
    '''Stops training if validation loss doesn't improve for `patience` epochs,
    unless the last 3 losses improved consecutively.'''

    def __init__(self, patience=5, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.consecutive_improvements = 0
        self.min_validation_loss = float('inf')
        self.previous_loss = float('inf')

    def early_stop(self, validation_loss):
        stop = False

        # If loss improved from the previous epoch
        if validation_loss < self.previous_loss - self.min_delta:
            self.consecutive_improvements += 1
            print(f"Loss improved. Consecutive improvements: {self.consecutive_improvements}")
        else:
            self.consecutive_improvements = 0

        # If new minimum loss is found
        if validation_loss < self.min_validation_loss - self.min_delta:
            self.min_validation_loss = validation_loss
            self.counter = 0
            print(f"New minimum validation loss: {self.min_validation_loss}. Counter reset.")
        else:
            # Only increment counter if no new min and not in the 3-batch improvement streak
            if self.consecutive_improvements < 3:
                self.counter += 1
                print(f"No new min. Counter incremented to {self.counter}")
            elif self.consecutive_improvements < 10:
                self.counter = 0
                print(f"Consecutive improvements between 3 and 10. Counter reset to 0")
            else:
                self.counter = 0
                self.min_validation_loss = validation_loss
                print(f"Since it improved for 10 epochs consecutively, but is still not better than the min_validation, the min validation loss is set to the current loss: {validation_loss}")

        if self.counter >= self.patience:
            stop = True
            print("Early stopping triggered.")

        self.previous_loss = validation_loss
        return stop

    
class EarlyStopperNSE:
    '''This class helps to stop training if the validation NSE is not increasing over certain number of epochs (patience)'''
    def __init__(self, patience= 5, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.max_NSE = -100000000
    
    def early_stop(self, NSE):
        if (NSE >= self.max_NSE):
            self.max_NSE = NSE
            self.counter = 0
        elif NSE <= (self.max_NSE - self.min_delta):
            self.counter += 1
            if(self.counter) >= self.patience:
                return True
        return False