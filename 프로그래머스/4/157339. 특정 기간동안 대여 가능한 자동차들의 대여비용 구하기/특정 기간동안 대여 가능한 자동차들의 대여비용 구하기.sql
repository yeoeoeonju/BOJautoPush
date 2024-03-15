-- 코드를 입력하세요

select A.CAR_ID, A.CAR_TYPE, ROUND(DAILY_FEE*30*((100-DISCOUNT_RATE)/100),0) as FEE
from (select * from CAR_RENTAL_COMPANY_CAR where CAR_TYPE in ('세단', 'SUV')) as A
    left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as B 
        on A.CAR_TYPE = B.CAR_TYPE and DURATION_TYPE = '30일 이상'
where CAR_ID not in (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where ("2022-11-01" between START_DATE and END_DATE)
        or ("2022-11-31" between START_DATE and END_DATE)) 
group by CAR_ID
having FEE >= 500000 and FEE < 2000000
order by FEE desc, A.CAR_TYPE, A.CAR_ID desc