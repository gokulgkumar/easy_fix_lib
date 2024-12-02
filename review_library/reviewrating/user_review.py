import string

class FeedbacksAnalyzer:
    def save_feedback(self, instructionModel,id, user, user_feedback,UserModel,FeedbackModel):
        """
        Saves feedback for a specific instruction along with the user's rating and sentiment analysis.
    """
       
        positive_keywords=None
        negative_keywords=None

        comment = self.analyzing_feedback(user_feedback)
        
        instructions = instructionModel.objects.get(id=id)
        User=UserModel.objects.get(id=user)
     
        feedbacksave = instructions.feedbacks.create(
            user=User, ins_id=id ,instruction=instructions.ins_type, feedback = user_feedback,comment=comment)
        return feedbacksave
     
    def analyzing_feedback(self, user_feedback, positive_keywords=None, negative_keywords=None):
        """
        Analyzes feedback text and determines if it's positive, negative, or neutral.
        """
        print(f"Original Feedback Text: {user_feedback}")  
        if positive_keywords is None:
            positive_keywords = ["good", "excellent", "helpful", "amazing", "great","brilliant","satisfied","impressive","helpful","nice","wonderful"]
        if negative_keywords is None:
            negative_keywords = ["bad", "poor", "confusing", "unhelpful", "terrible","useless","not worth","waste", "scam"]

        # Convert feedback text to lowercase and split into words
        words = user_feedback.lower().translate(str.maketrans('', '', string.punctuation)).split()
    
        # Initialize counters for positive and negative matches
        positivefeed_count = 0
        negativefeed_count = 0
    
        # Check each word against the keywords
        for word in words:
            if word in positive_keywords:
                positivefeed_count += 1
            if word in negative_keywords:
                negativefeed_count += 1
        if positivefeed_count > negativefeed_count:
            return "positive"
        elif negativefeed_count > positivefeed_count:
            return "negative"
        return "neutral"
