

Drop Table if EXISTS GameInfo
Drop Table if EXISTS Sales
CREATE TABLE Sales(
    [Rank] int primary key,
	[Total_Shipped] [float] NULL,
	[Global_Sales] [float] NULL,
	[NA_Sales] [float] NULL,
	[PAL_Sales] [float] NULL,
	[JP_Sales] [float] NULL,
	[Other_Sales] [float] NULL
)

CREATE TABLE GameInfo (
    [Rank] int primary key,
	[Name] [nvarchar](max) NULL,
	[Genre] [nvarchar](max) NULL,
	[ESRB_Rating] [nvarchar](max) NULL,
	[Platform] [nvarchar](max) NULL,
	[Publisher] [nvarchar](max) NULL,
	[Developer] [nvarchar](max) NULL,
	[Critic_Score] [float] NULL,
	[User_Score] [float] NULL,
    [Year] [int] NULL
    CONSTRAINT FK_GameInfo_Sales
        FOREIGN KEY (Rank) -- field on this Table
        REFERENCES Sales(Rank) -- what table do we refer to and what field do we refer to
)
