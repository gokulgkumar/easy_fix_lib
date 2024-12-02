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

    def rating_save(self, instruction, instruction_id, user_id, rating):
        """
        Save a rating for a repair or maintenance instruction.
        """
        # Save the rating using the corresponding model
        instruction = instruction.objects.get(id=instruction_id)
        rating_obj = instruction.ratings.create(user=user_id, rating=rating)
        return rating_obj
