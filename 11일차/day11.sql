use sqldb;
select * from buytbl;
select * from usertbl;

select userid,
	sum(price * amount) as '총 구매액',
    case when sum(price * amount) < 200 then '새싹고객'
		 when sum(price * amount) < 1500 then '우수고객'
         else 'vip 고객' end as '고객구분'
    from buytbl
    group by userid
    order by 2;
    
select prodName from buytbl where groupName is not null;
    
select prodName from buytbl where length(groupName) < 1;


select prodName from buytbl where length(ifnull(groupName, '')) <1;
-- 대체하고 체크하기
select distinct prodName, ifnull(groupName,'미분류') as groupName from buytbl;

alter table usertbl add pwd varchar(20);
update usertbl set pwd=concat(userid,right(birthyear,2),'1234');
select * from usertbl;

select userid, mdate from usertbl where right(mDate,5) like '07%'; 

select userid, mdate, timestampdiff(year,mdate,curdate()) as aa
	from usertbl
    where month(mdate) = month(curdate());
    
create table maxtbl(col1 longtext, col2 longtext);

insert into maxtbl values (repeat('a',1000000), repeat('가',1000000));
select length(col1), length(col2) from maxtbl;

select userid, name, mdate, 
	case when month(mdate) in (12,1,2) then '겨울'
    when month(mdate) in (3,4,5) then '봄'
    when month(mdate) in (6,7,8) then ' 여름'
    when month(mdate) in (9,10,11) then '가을'
    end as '계절'
    from usertbl;
    

select  
	sum(if(month(mdate) in (12,1,2),1,0)) as '겨울',
    sum(if(month(mdate) in (3,4,5),1,0 )) as '봄',
    sum(if(month(mdate) in (6,7,8),1,0 )) as ' 여름',
    sum(if(month(mdate) in (9,10,11),1,0 )) as '가을'
    from usertbl;
    
    -- json
select json_object('name',name,'height',height, 'id',userid)
	from usertbl
    where userid = 'BBK';
    
select count(distinct userid) from buytbl;

select *
	from buytbl
    inner join usertbl
		on buytbl.userID = usertbl.userID
	where usertbl.userID = 'bbk';
    

select b.userID,
	u.name, b.prodname, u.addr, 
    u.mobile1 + u.mobile2 as '연락처'
	from buytbl b inner join usertbl u
	on b.userID = u.userID;
        
select buytbl.userID, name, prodname, addr, mobile1 + mobile2 as '연락처'
	from buytbl, usertbl
    where buytbl.userID = usertbl.userID;
    
select b.userID, name, prodname, addr, mobile1 + mobile2 as '연락처'
	from buytbl b, usertbl u
    where b.userID = u.userID
	and b.userid = 'bbk';
    
select b.userID, name, prodname, addr, mobile1 + mobile2 as '연락처'
	from buytbl b inner join usertbl u
    on b.userID = u.userID
	where b.userid = 'bbk';
    
select u.userID, u.name, u.addr, sum(b.price * b.amount) as '총구매액'
	from usertbl u
		inner join buytbl b on b.userID = u.userID
    group by u.userid
    order by u.userid;
    
select u.userID, u.name, u.addr
	from usertbl u
    where exists (
		select *
        from buytbl b
        where u.userID = b.userID);

-- left outer join        
use sqldb;
select u.userid, u.name, b.prodname, u.addr
	from usertbl u
	left outer join buytbl b
    on u.userID = b.userID;
    
-- union, union all, self join

create view v_usertbl
AS
	select userid, name, addr from usertbl;
select * from v_usertbl;

select a.*, b.price
from v_usertbl a, sqldb.buytbl b
where a.userid = b.userid;