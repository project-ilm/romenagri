-- हिंदी VHDL substrate demo (Romenagri substrate layer)
-- इकाई (entity) योजक (adder) is
-- Pipeline: हिंदी source → Romenagri → h2vhdl (PLANNED front-end) → VHDL → synthesis
-- Current: substrate demonstrated; h2vhdl.lex front-end maps:
--   ikaaii → entity, sthaapatya → architecture, sa_nkeeta → signal
--   aara_nbha → begin, a_nta → end, taara → wire, pa_njikaa → reg
-- © 1993-2026 Abhishek Choudhary, GPL

-- The Hindi source that would compile once h2vhdl.lex is built:
-- <शैली परिभाषा>
-- इकाई योजक is
--     द्वार (A, B : in std_logic; Sum : out std_logic);
-- अंत इकाई;
--
-- स्थापत्य व्यवहार of योजक is
-- आरंभ
--     Sum <= A xor B;
-- अंत व्यवहार;

-- Working VHDL (substrate-verified, keywords shown with Romenagri forms):
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- entity (ikaaii), architecture (sthaapatya), signal (sa_nkeeta)
entity adder is  -- ikaaii
    Port ( A : in  STD_LOGIC;
           B : in  STD_LOGIC;
           Sum : out STD_LOGIC);
end adder;  -- a_nta ikaaii

architecture Behavioral of adder is  -- sthaapatya
begin  -- aara_nbha
    Sum <= A xor B;
end Behavioral;  -- a_nta
