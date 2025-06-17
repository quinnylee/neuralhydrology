import logging
logger = logging.getLogger(__name__)


class EarlyStopper:
    """Stops training if validation loss doesn't improve for `patience` epochs,
    unless the last round(patience/3) losses improved consecutively."""

    def __init__(self, patience: int, min_delta: float):
        self._patience = patience
        self._min_delta = min_delta
        self._counter = 0
        self._consecutive_improvements = 0
        self._min_validation_loss = float('inf')
        self._previous_loss = float('inf')

    def check_early_stopping(self, validation_loss):
        stop = False

        # If loss improved from the previous epoch
        if validation_loss < self._previous_loss - self._min_delta:
            self._consecutive_improvements += 1
            logger.info(f"Loss improved. Consecutive improvements: {self._consecutive_improvements}")
        else:
            self._consecutive_improvements = 0

        # If new minimum loss is found
        if validation_loss < self._min_validation_loss - self._min_delta:
            self._min_validation_loss = validation_loss
            self._counter = 0
            logger.info(f"New minimum validation loss: {self._min_validation_loss}. Counter reset.")
        else:
            # Only increment counter if no new min and not in the 1/3rd of patient batch improvement streak
            if self._consecutive_improvements < int(round(self._patience / 3)):
                self._counter += 1
                logger.info(f"No new min. Counter incremented to {self._counter}")   
            elif self._consecutive_improvements < int(round(self._patience / 2)):
                self._counter = 0
                logger.info(f"Consecutive improvements between 3 and 10. Counter reset to 0")
            else:
                self._counter = 0
                self._min_validation_loss = validation_loss
                logger.info(f"Since it improved for 10 epochs consecutively, but is still not better than the min_validation, the min validation loss is set to the current loss: {validation_loss}")

        if self._counter >= self._patience:
            stop = True
            logger.info("Early stopping triggered.")

        self._previous_loss = validation_loss
        return stop