class RatingAnalyzer:
    """
    A class to handle ratings for repair and maintenance instructions.
    """

    def __init__(self, user_rating=(1, 5)):
        self.user_rating = user_rating

    def check_rating(self, rating):
        """
        Ensure the rating is within the allowed range.
        """
        if rating < self.user_rating[0] or rating > self.user_rating[1]:
            raise ValueError(f" the rating should be in the range of {self.user_rating[0]} and {self.user_rating[1]}")
        return True

    def average_rating(self, ratings):
        """
        Calculate the average rating from a list of ratings.
        """
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)

    def rating_save(self, inst, id, user, user_rating,UserModel):
        """
        Save a rating for a repair or maintenance instruction.
        """
        # Save the rating using the corresponding model
        instructions = inst.objects.get(id=id)
        print(f"Instruction Class: {instructions.ins_type}")
        
        User_log=UserModel.objects.get(id=user)
        
        
        print('hello')
        print(f"Instruction Class: {inst}")
        print(f"Instruction ID: {id}")
        print(f"User ID: {user}")
        print(f"Rating: {user_rating}")
        print('UserModel',User_log)
      
        if instructions.ins_type=='Maintenance':
            
            
            rating_obj = instructions.ratings.create(user=User_log, rating=user_rating,ins_id=id,instruction=instructions.ins_type)
            return rating_obj
        else:
            rating_obj = instructions.ratings.create(user=User_log, rating=user_rating,ins_id=id,instruction=instructions.ins_type)
            return rating_obj
            
        
        
        
