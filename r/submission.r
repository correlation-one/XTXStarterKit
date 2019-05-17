input<-file('stdin', 'r')

get_next_data <- function() {
  readLines(input, n=1)
}

submit_prediction <- function(pred) {
  cat(paste(pred, "\n"), sep="")
}


### Basic sample algorithm
while (TRUE) {
  tryCatch({
    ### Read data
    data <- get_next_data()

    ### Guess 3 every time
    submit_prediction(1)
  }, error=function(e){})
} 
