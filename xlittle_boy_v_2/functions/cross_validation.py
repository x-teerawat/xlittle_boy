def cross_validation(self):
    ### Reverse cross validation
    if self.IsCrossValidation == True:
        self.x = self.x[::-1, :, :]
        self.y = self.y[::-1, :]
        
        # print("After cross validation")
        # print(f"self.x: \n{self.x}")
        # print(f"self.x.shape: \n{self.x.shape}")
        # print(f"self.y: \n{self.y}")
        # print(f"self.y.shape: \n{self.y.shape}")