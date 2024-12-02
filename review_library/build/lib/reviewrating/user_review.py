class FeedbacksAnalyzer:
    """
    A class to process and analyze feedbacks for repair and maintenance instructions.
    """

    def __init__(self):
        pass

    def format_UserFeedbacks(self, feedbacks):
        """
        Clean and format feedbacks text.
        """
        return feedbacks.strip().capitalize()

    def analyze_UserFeedbacks(self, feedbacks):
        """
        Analyze feedbacks to determine if it's positive, negative, or neutral.
        """
        positive_review_keywords = ["clear", "helpful", "easy", "excellent", "good","impressive","brilliant"]
        negative_review_keywords = ["unclear", "confusing", "difficult", "bad", "poor","useless"]

        feedbacks_lowerCase = feedbacks.lower()
        
        if any(word in feedbacks_lowerCase for word in positive_review_keywords):
            return "positive feedback by the user"
        elif any(word in feedbacks_lowerCase for word in negative_review_keywords):
            
            return "negative feedback by the user"
        return "neutral feedback by the user"

    def save_UserFeedbacks(self, instructions, instruction_id, user_id, feed_text, comment):
        """
        Save feedbacks for a repair or maintenance instruction.
        """
        instruction = instructions.objects.get(id=instruction_id)
        user_feedbacks = instruction.feedbacks.create(user_id=user_id, feedback_text=feed_text, comment=comment)
        return user_feedbacks
