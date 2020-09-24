# VirtualBox 네트워크

## 호스트 OS와 통신
1. 호스트 네트워크 추가
2. 어댑터 설정에서 '호스트 전용 어댑터' 선택
3. 무작위 모드 메뉴에서 '가상 머신에 허용' 선택
4. 게스트 OS에서 ifconfig 로 ip 확인

## 가상OS 에서 외부 서버로 통신
1. 어댑터 설정에서 'NAT' 선택
2. /etc/sysconfig/network-scripts/ifcfg-enp0s3 수정
    1. ONBOOT=yes 로 설정
3. ifconfig 로 ip 확인