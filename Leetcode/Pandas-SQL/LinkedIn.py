import pandas as pd
import numpy as np
'''============================================================================================================='''
'''
Question1 - 欺诈与找到访问home之后访问最频繁的页面

|datetime|            memberId| pageId|
|2019-01-15 08:00:00|     100|   home|
|2019-01-15 08:00:01|     100|   home|
|2019-01-15 08:00:05|     100|network|
|2019-01-15 08:00:16|     100|   jobs|
|2019-01-15 08:00:20|     100|   home|
|2019-01-15 08:00:00|     200|   home|
|2019-01-15 08:00:05|     200|   home|
|2019-01-15 08:00:12|     200|network|
|2019-01-15 08:00:20|     200|   jobs|
|2019-01-15 08:00:25|     200|network|
|2019-01-15 08:00:00|     300|   home|
|2019-01-15 08:00:04|     300|network|
|2019-01-15 08:00:10|     300|   home|
|2019-01-15 08:00:10|     300|   home|
|2019-01-15 08:00:20|     300|   jobs|
Q1: 同memberId在一秒内登录两次以上home page, 除了第一次外都看做fraud，return fraud records.
Q2: 去掉fraud之后，member最喜欢在访问home之后访问什么pageId, return pageId.
'''
# SQL Q1: 可以建一个新field，is_fraud helps to filter out those fraud records. Also help for next step analysis.
select
  l1.datetime,
  l1.memberId,
  l1.pageId
from u_login as l1
inner join
u_login as l2
on l1.memberId = l2.memberId
and STR_TO_DATE(l1.datetime,'%Y-%m-%d %H:%i:%s') - STR_TO_DATE(l2.datetime,'%Y-%m-%d %H:%i:%s') =1
union all
select
  datetime,
  memberId,
  pageid
from u_login
where pageId = 'home'
group by datetime, memberID
having count(*)>1;

# SQL Q2:
with cte as
(
select
  distinct
  datetime,
  memberId,
  pageId,
  row_number() over (partition by memberId order by datetime) as rn
from u_login
)
, page_id_cnt as (
select
  c2.pageId,
  dense_rank() over (order by count(c2.pageId) desc) as dense_rk
from cte as c1
inner join cte as c2
on c1.memberId = c2.memberId and c1.rn = c2.rn - 1 and c1.pageId = 'home' and c2.pageId <> 'home'
group by c2.pageId
)
select pageId
from page_id_cnt
where dense_rk = 1
;

# Python Q1:
df_filter_home = data.loc[data['pageId'] == 'home'].reset_index(drop=True)
df_count = df_filter_home.groupby(['datetime', 'memberId'])['pageId'].count().to_frame('num_pageId').reset_index()
df_duplicate = df_count.loc[df_count['num_pageId'] > 1].rename({'num_pageId':'pageId'}, axis =1)
df_join = df_filter_home.merge(df_filter_home, how = 'inner', left_on = 'memberId', right_on = 'memberId')
df_gap = df_join.loc[(pd.to_datetime(df_join['datetime_x']) - pd.to_datetime(df_join['datetime_y'])).dt.total_seconds() == 1].reset_index(drop=True)
df_gap = df_gap[['datetime_x','memberId','pageId_x']].rename({'datetime_x': 'datetime', 'pageId_x': 'pageId'}, axis=1)
df_duplicate.loc[:, 'pageId']= 'home'
df_fraud = pd.concat([df_gap, df_duplicate])
df_fraud

# Python Q2:
remove_fraud = data.drop_duplicates()
remove_fraud['rn'] = remove_fraud.sort_values('datetime', ascending = True).groupby('memberId').cumcount() + 1
data_join = remove_fraud.merge(remove_fraud, how = 'inner', left_on = 'memberId', right_on = 'memberId')
data_filter = data_join.loc[(data_join['rn_x'] == data_join['rn_y']-1) & (data_join['pageId_x'] == 'home') & (data_join['pageId_y'] != 'home')]['pageId_y'].to_frame()
res = data_filter.pageId_y.mode().to_frame('pageId')

'''
'''============================================================================================================='''
'''
Question2 - 微软谷歌跳槽
data = {'Member_id':[1,1,1,2,2,2],
        'Company': ['MS','Google','Facebook','MS','Oracle','Google'],
        'Year_Start': [2000, 2006,2012,2001,2004,2007]}
df = pd.DataFrame(data)
'''
# 2.1 有多少人离开了微软去了Google
# SQL:

SELECT count(distinct t1.member_id)
FROM table t1  join table t2 on t1.member_id = t2.member_id
WHERE t1.year_start <= t2.year_start
AND t1.company_name = "microsoft" AND t2.company_name ="google";

# Python:
# A member could join Google at the same year as Microsoft? If so, >=0 make sense otherwise >0 only
df_join = pd.merge(df, df, on = ['Member_id'], how = 'inner')
df_filter = df_join.loc[(df_join.Company_x == 'Microsoft') & \
                        (df_join.Company_y == 'Google') & \
                        (df_join.Year_Start_y - df_join.Year_Start_x >=0)]
df_filter['Member_id'].nunique()

# 2.2 有多人直接从微软去了Google
# SQL:
with cte as (
select
    Member_id,
    Company,
    row_number() over (partition by Company order by Year_Start) as rn
from table
)
select
    count(distinct t1.Member_id)
from cte as t1
inner join cte as t2
 on t2.rn - t1.rn = 1 and t1.Company = 'Microsoft' and t2.Company = 'Google'

# Python:
df['RN'] = df.sort_values('Year_Start', ascending = True) \
            .groupby('Member_id') \
            .cumcount() + 1
df_join = pd.merge(df, df, on = 'Member_id', how = 'inner')
df_filter = df_join[(df_join.Company_x == 'Microsoft') & (df_join.Company_y == 'Google') & (df_join.RN_y - df_join.RN_x == 1)]
df_filter['Member_id'].nunique()

'''
'''============================================================================================================='''
'''
Question 3 - 更新member id action

表 status:
Member_id   Status
1            on
2            off
3            on
4            off

表 action:
Member_id   date_sk   action
1           7/2       turn_off
1           7/5       turn_on
2           7/3       turn_on
4           7/10      turn_on
4           7/13      turn_off

status_table = {'Member_id':[1,2,3,4],
        'status': ['on', 'off', 'on', 'off'],
        }
df_status = pd.DataFrame(status_table)

actions_table = {'Member_id':[1,1,2,4,4],
        'date_sk': ['7/2','7/5','7/3','7/10','7/13'],
        'action': ['turn_off', 'turn_on', 'turn_on', 'turn_on', 'turn_off']}
df_actions = pd.DataFrame(actions_table)
'''
# SQL Solution:
select
	coalesce(s.member_id, a.member_id) as member_id,
	case when status is null then current_status
		 when current_status is null then status
		 else current_status
	end as current_status
from
status_table as s
full join
(
	select
		member_id,
		current_status
	from
	(
		select
			member_id,
			date_sk,
			right(action, len(action) - charindex('_', action)) as current_status,
			row_number() over (partition by member_id order by date_sk desc) as rn
		from action_table
	) t
) a
on s.member_id  = a.member_id

# Python solution: transform 相当于建了一个新的dataframe
df1=df_actions[df_actions.groupby('Member_id')['date_sk'].transform(max)==df_actions['date_sk']]
df1['current_status'] = df1['action'].apply(lambda x: x.split('_')[1])
df_join = pd.merge(df_status, df1, left_on = 'Member_id', right_on = 'Member_id', how = 'outer')
df_join['current_status'].fillna(df_join['status'], inplace = True)
df_final = df_join[['Member_id', 'current_status']]
df_final

'''
'''============================================================================================================='''
'''
Question 4 - Job view and application
判断机器人的方法是view时间在申请之前，机器人的记录不会出现在view表里. 例如下表FACT_JOB_APPLICATIONS中，
Member 2申请Job B的第一条记录就是机器人
FACT_JOB_VIEW
#=====
JOB MEMBER_ID TIMESTAMP
A     1       01/01/2020
A     1       01/01/2020
B     1       01/01/2020
A     2       01/02/2020
B     2       01/10/2020
FACT_JOB_APPLICATIONS
#=====
JOB MEMBER_ID TIMESTAMP
A     1       01/02/2020
B     2       01/08/2020
B     2       01/12/2020
'''
# Q1: output job, total_view, unique_viewer, num_unique_applicant
SELECT t1.job,
    COUNT(t1.member_id) AS total_view,
    COUNT(DISTINCT t1.meber_id) AS unique_viewer,
    COUNT(DISTINCT t2.member_id) AS unique_appicant
FROM FACT_JOB_VIEW t1
LEFT JOIN FACT_JOB_APPLICATIONS t2
ON t1.job = t2.job
GROUP BY t1.job

# Q2: We suspect bots are applying to our jobs without triggering a job view.
# Modify the query to only count applications where the member actually viewed the Job on or before the application date.
SELECT t1.job, t1.total_view, t1.unique_viewer, t2.unique_appicant
FROM (
SELECT job, COUNT(member_id) AS total_view, COUNT(DISTINCT member_id) AS unique_viewer FROM FACT_JOB_VIEW GROUP BY job) t1
LEFT JOIN (
SELECT a2.job, COUNT(DISTINCT a2.member_id) AS unique_appicant
FROM FACT_JOB_VIEW a1
LEFT JOIN FACT_JOB_APPLICATIONS a2
ON a1.job = a2.job AND a1.member_id = a2.member_id AND a1.timestamp <= a2.timestamp GROUP BY a2.job) t2
ON t1.job = t2.job

'''============================================================================================================='''
'''
Question 5 - Job posting

job_id, member_id, job_posting_date
1001      1         2017-04-14
1002      1         2017-08-14
1003      2         2017-05-31
1004      3         2016-08-23
1005      3         2017-04-28
1006      3         2017-05-23
1007      3         2017-07-08
new job posting: 每个 member post 的第一个 job posting
repeat job posting: 除了第一个 其他的
'''
# Q1: 求number of new job posts
# SQL:
select
        count(p.job_id) as num_new_job_posts
from post as p
inner join
        (
                select
                        member_id,
                        min(job_posting_date) as first_posting_date,
                        max(job_posting_date) as last_posting_date
                from post
                group by member_id
        ) as t
on p.member_id = t.member_id
and p.job_posting_date = t.first_posting_date
and p.job_posting_date = t.last_posting_date

#Python:
job_post_member = job_post.groupby('member_id') \
                          .agg(first_posting_date = ('job_posting_date', 'min'),
                               last_posting_date = ('job_posting_date', 'max')) \
                          .reset_index()

job_post_join = job_post.merge(job_post_member, how = 'inner', left_on = 'member_id', right_on = 'member_id')
job_post_join_filter = job_post_join.loc[(job_post_join['job_posting_date'] == job_post_join['first_posting_date']) \
                  & (job_post_join['job_posting_date'] == job_post_join['last_posting_date'])]
res1 = job_post_join_filter['member_id'].count()

# Q2: 求number of repeat job posts
# SQL:
select
        count(job_id) as num_repeated_job_posts
from
        (
        select
                job_id,
                memeber_id,
                row_number() over (partition by member_id order by job_posting_date) as rn
        from post
        ) t
where rn > 1

# Python:
job_post['rn'] = job_post.sort_values('job_posting_date', ascending = True).groupby('member_id').cumcount() + 1
job_repeat = job_post.loc[job_post['rn'] > 1]
res2 = job_repeat['member_id'].count()
res2

# Q3: 如果一个人超过180天没发帖，180天后发的贴是reactivated posts，求number of reactivated posts
# SQL:
with cte_post as (
	select
		job_id,
		memeber_id,
		job_posting_date,
		row_number() over (partition by member_id order by job_posting_date) as rn
	from post
)
select
    count(p1.job_id)
from cte_post as p1
inner join cte_post as p2
on p1.member_id = p2.member_id and datediff(p1.job_posting_date, p2.job_posting_date) >= 180
and p1.rn - 1 = p2.rn

# Python:
job_post['rn'] = job_post.sort_values('job_posting_date', ascending = True).groupby('member_id').cumcount() + 1
job_post_join = job_post.merge(job_post, how = 'inner', left_on = 'member_id', right_on = 'member_id')
job_post_filter = job_post_join.loc[((pd.to_datetime(job_post_join['job_posting_date_x']) - pd.to_datetime(job_post_join['job_posting_date_y'])).dt.total_seconds() >= 180*24*60*60) \
                    & (job_post_join['rn_y'] == job_post_join['rn_x'] - 1)]
job_post_filter['job_id_x'].count()

'''
'''==========================================================================================='''
'''
Question 6 - Video post
video post
post_date  member_id  video_length
2018-12-18   123        95
2018-12-18	 576	    65
2018-12-19	 576	    22
2018-12-18	 123	    20
2018-12-20	 260	    100
2018-12-21	 450	    150
2018-12-22	 123	    200

member_id  country   join_date
123	        USA	     2018-11-03
576	        UK	     2016-05-15
807	        AUS	     2012-04-12
260	        UK	     2018-12-20
450	        India	 2019-01-12
'''
# 1 SQL: How many members post their first video on the same day they've joined the platform?
SELECT COUNT(DISTINCT v.memberid) AS num
FROM video_posts v
JOIN members m
ON v.memberid = m.memverid AND v.post_date = m.join_date
# 1 Python: How many members post their first video on the same day they've joined the platform?
df_join = video_posts.merge(members, how = 'inner', left_on = 'member_id', right_on = 'member_id')
df_filter = df_join.loc[df_join.post_date == df_join.join_date]
df_filter.member_id.nunique()

# 2 SQL: How many members from each country have posted a video longer than 60 seconds?
SELECT m.country, COUNT(DISTINCT v.memberid) AS num
FROM
(
        SELECT
                memberid
        FROM video_posts
        WHERE video_length > 60
) AS v
JOIN members m
ON v.memberid = m.memverid
GROUP BY m.country
# 2 Python: How many members from each country have posted a video longer than 60 seconds?
video_longer_60 = video_posts.loc[video_posts.video_length > 60]
df_join = video_longer_60.merge(members, how = 'inner', left_on = 'member_id', right_on = 'member_id')
res = df_join.groupby('country').agg({'member_id': pd.Series.nunique}).reset_index()

# 3 SQL: Python: We hypothesize that our video posting features might not be catching on as well internationally as they do in the US.
# Do US members upload more videos than non-US members
SELECT
    CASE WHEN country = 'US' THEN 'US'
    ELSE 'NON-US'
    END AS country_group,
    AVG(num_post) AS avg_post
FROM
(
    SELECT
        m.country,
        v.post_date AS date,
        COUNT(v.*) / COUNT(DISTINCT v.memberid) AS num_post
    FROM video_posts v
    JOIN members m
    ON v.memberid = m.memverid
    GROUP BY m.country, v.post_date) tmp
GROUP BY country_group

# 3 Python: We hypothesize that our video posting features might not be catching on as well internationally as they do in the US.
# Do US members upload more videos than non-US members
df_join = video_posts.merge(members, how = 'inner', left_on = 'member_id', right_on = 'member_id')
df_avg_country_per_day = df_join.groupby(['country', 'post_date'])['member_id'].agg(['count','nunique']) \
                                .rename({'count':'total_cnt', 'nunique':'unique_cnt'}, axis = 1).reset_index()
df_avg_country_per_day['avg_post_per_country_date'] = df_avg_country_per_day['total_cnt']//df_avg_country_per_day['unique_cnt']
df_avg_country_per_day.groupby('country').agg({'avg_post_per_country_date': 'mean'})
'''
'''==========================================================================================='''
'''
Question 7 -  User Purchase Platform ** Only SQL LC 1127
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+
Output:
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+
'''
select
    l.spend_date,
    l.platform,
    coalesce(t1.total_amount, 0) as total_amount,
    coalesce(t1.total_users, 0) as total_users
from
(
    select distinct spend_date, 'desktop' as platform from Spending union all
    select distinct spend_date, 'mobile' as platform from Spending union all
    select distinct spend_date, 'both' as platform from Spending
) l
LEFT JOIN (
select
    spend_date,
    platform,
    sum(total_amount) as total_amount,
    count(user_id) as total_users
from
(
select
    spend_date,
    user_id,
    case when count(user_id) = 1 then platform
         else 'both'
    end as platform,
    sum(amount) as total_amount
from spending
group by spend_date, user_id
) t
group by spend_date, platform
) t1
on l.spend_date = t1.spend_date and l.platform = t1.platform
'''
'''==========================================================================================='''
'''
Question 8: Email combinations
+-----+------------------------+
| id  | email                  |
+-----+------------------------+
| 100 | M100_Email_1@gmail.com |
| 100 | M100_Email_2@gmail.com |
| 100 | M100_Email_3@gmail.com |
| 100 | M100_Email_4@gmail.com |
| 200 | M200_Email_1@gmail.com |
| 200 | M200_Email_2@gmail.com |
| 200 | M200_Email_3@gmail.com |
| 300 | M300_Email_1@gmail.com |
| 300 | M300_Email_2@gmail.com |
+-----+------------------------+
Output:
+-----+------------------------+------------------------+
| id  | email                  | email                  |
+-----+------------------------+------------------------+
| 100 | M100_Email_1@gmail.com | M100_Email_2@gmail.com |
| 100 | M100_Email_2@gmail.com | M100_Email_3@gmail.com |
| 100 | M100_Email_1@gmail.com | M100_Email_3@gmail.com |
| 100 | M100_Email_3@gmail.com | M100_Email_4@gmail.com |
| 100 | M100_Email_2@gmail.com | M100_Email_4@gmail.com |
| 100 | M100_Email_1@gmail.com | M100_Email_4@gmail.com |
| 200 | M200_Email_1@gmail.com | M200_Email_2@gmail.com |
| 200 | M200_Email_2@gmail.com | M200_Email_3@gmail.com |
| 200 | M200_Email_1@gmail.com | M200_Email_3@gmail.com |
| 300 | M300_Email_1@gmail.com | M300_Email_2@gmail.com |
+-----+------------------------+------------------------+
'''
SQL: 找到不同的组合，不能重复

with cte as (
select
    id,
    email,
    substring_index(substring_index(email, '@',1),'_',-1) as rn   # substring_index(email, '@',1) return @分开后第一个位置 M300_Email_1, -1 return 1
from member_email
)
select
    c1.id,
    c1.email,
    c2.email
from cte as c1
inner join cte as c2
on c1.id = c2.id and c1.rn < c2.rn
;

Python: 找到不同的组合，不能重复
member_email['rn'] = member_email['email'].apply(lambda x: x.split('@')[0].split('_')[-1])
df_join = member_email.merge(member_email, how = 'inner', left_on = 'id', right_on = 'id', suffixes = ['_1', '_2'])
df_filter = df_join.loc[df_join['rn_1'] < df_join['rn_2']]
df_res = df_filter[['id', 'email_1', 'email_2']]
df_res

'''
'''==========================================================================================='''
Question 9 Article view <LC 1148, 1149>
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
'''
<1> SQL: 多少 author 曾经没看过自己的文章?
SELECT COUNT(DISTINCT author_id) AS num
FROM Views
WHERE author_id NOT IN (
    SELECT DISTINCT author_id FROM Views WHERE author_id = viewer_id)

<1> Python: 多少 author 曾经没看过自己的文章?
author_see_article = article.loc[article['author_id'] == article['viewer_id']].drop_duplicates()
author_nosee_article = article.loc[~article['author_id'].isin(author_see_article['author_id'])]
author_nosee_article['author_id'].nunique()

<2> SQL: 在某一天， 比如 '2018-08-02'， 有多少读者看了 1 篇以上文章
SELECT COUNT(DISTINCT viewer_id)
FROM article_views
WHERE view_date = '2018-08-02'
GROUP BY viewer_id
HAVING COUNT(DISTINCT article_id) > 1

<2> Python:在某一天， 比如 '2018-08-02'， 有多少读者看了 1 篇以上文章
viewer_date = article.loc[article['view_date'] == '2019-08-02']
viewer_group = viewer_date.groupby('viewer_id').agg({'article_id': 'nunique'}).reset_index()
viewer_group_filter = viewer_group.loc[viewer_group['article_id'] > 1]
viewer_group_filter['viewer_id'].nunique()
