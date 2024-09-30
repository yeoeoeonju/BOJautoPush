-- 코드를 작성해주세요
select count(*) as COUNT
from ecoli_data
where
CONV(genotype,10,2) = '1' or
CONV(genotype,10,2) like '%001' or
CONV(genotype,10,2) like '%100' or
CONV(genotype,10,2) like '%101'