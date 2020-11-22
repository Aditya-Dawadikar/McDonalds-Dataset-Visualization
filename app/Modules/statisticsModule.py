import statistics as stat

class statisticsModule:
    def __init__(self):
        self.stat=stat
        
    #methods for operating on list
    def getMin(self,data):
        return min(data)
    
    def getMax(self,data):
        return max(data)
    
    def getMean(self,data):
        return self.stat.mean(data)
    
    def getMode(self,data):
        #note: getMode will return the mode value for the list if there exists atleast one repeating value else it returns None
        try:
            result= self.stat.mode(data)
            return result
        except:
            return None
    
    def getMedian(self,data):
        return self.stat.median(data)
    
    def getVariance(self,data):
        return self.stat.variance(data)
    
    def getStandardDeviation(self,data):
        return self.stat.stdev(data)
    
    #methods to operate on dataframeMap
    #eg: dataframeMap={'calories':[1,2,3,4,5,6,7,8],'sodium':[1,2,3,4,5,6,7,8,9]}

    def getMinFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getMin(dataframeMap[column])
        return result
    
    def getMaxFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getMax(dataframeMap[column])
        return result
                          
    def getMeanFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getMean(dataframeMap[column])
        return result
    
    def getModeFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getMode(dataframeMap[column])
        return result
    
    def getMedianFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getMedian(dataframeMap[column])
        return result
    
    def getVarianceFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getVariance(dataframeMap[column])
        return result
    
    def getStandardDeviationFromDataset(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getStandardDeviation(dataframeMap[column])
        return result
    
    #method for column summary
    def getSummary(self,data):
        result={}
        result['row count']=len(data)
        result['minimum']=self.getMin(data)
        result['maximum']=self.getMax(data)
        result['mean']=self.getMean(data)
        result['mode']=self.getMode(data)
        result['median']=self.getMedian(data)
        result['variance']=self.getVariance(data)
        result['standard deviation']=self.getStandardDeviation(data)
        return result
    
    #method for dataframemap summary
    def getSummaryFromDataFrameMap(self,dataframeMap):
        result={}
        for column in dataframeMap:
            result[column]=self.getSummary(dataframeMap[column])
        return result