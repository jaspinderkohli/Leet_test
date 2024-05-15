class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        '''
            Example 1
            IP = [ 5, 4, 3, 2, 1] # Scoresss
            OP = [ Gold, Silver, Bronze, 4 , 5th]

            standings = [ 1, 2, 3, 4, 5]

            Example 2
            Input: 
            score = [10, 3, 8, 9, 4]
            sorted_score = [10, 9, 8, 4, 3]
            
            standings = []

            Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

            Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

        '''

        sorted_score = score.copy()
        sorted_score.sort(reverse=True)
        # print('score', score)
        # print('sorted_score', sorted_score)
        
        standings = ['None']* len(score)
        standing_map = {
            1 : 'Gold Medal',
            2 : 'Silver Medal',
            3 : 'Bronze Medal'
        }

        for idx_srt, x in enumerate(sorted_score):
            for idx_score, j in enumerate(score):
                if x == j:
                    # print('Athlete', x, ' Rank ', idx_srt+1 , ' pos in score', idx_score)
                    if (idx_srt+1) in standing_map.keys():
                        standings[idx_score] = standing_map[idx_srt+1]
                    else:
                        standings[idx_score] = str(idx_srt+1)
        # print('standings', standings)
        return standings


        
