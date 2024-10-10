-- 코드를 작성해주세요
select 
    year(DIFFERENTIATION_DATE) YEAR,
    (b.mx_size - SIZE_OF_COLONY) YEAR_DEV,
    id
from (
    select *, year(DIFFERENTIATION_DATE) year
    from ECOLI_DATA) a
join  
(select 
    year(DIFFERENTIATION_DATE) year, 
    max(SIZE_OF_COLONY) mx_size
from ECOLI_DATA
group by year) b
on  a.year = b.year
order by 1, 2