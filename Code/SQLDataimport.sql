
INSERT into Sales ([Rank], [Total_Shipped], [Global_Sales], [NA_Sales], [PAL_Sales], [JP_Sales], [Other_Sales])
    SELECT [Rank], [Total_Shipped], [Global_Sales], [NA_Sales], [PAL_Sales], [JP_Sales], [Other_Sales]
    FROM TotalShipped_Test

INSERT into GameInfo ([Rank], [Name], [Genre], [ESRB_Rating], [Platform], [Publisher], [Developer], [Critic_Score], [User_Score], [Year])
    SELECT [Rank], [Name], [Genre], [ESRB_Rating], [Platform], [Publisher], [Developer], [Critic_Score], [User_Score], [Year]
    FROM TotalShipped_Test

