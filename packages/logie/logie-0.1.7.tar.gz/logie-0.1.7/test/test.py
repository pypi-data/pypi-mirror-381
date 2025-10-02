import sys
import os
sys.path.append('/home/kimyh/library/logie')
import logie as lo

def main():
    log_path = os.getcwd()
    lo.log_del(
        log_path=os.path.join(log_path, 'log'),
        days=30
    )
    # log = lo.get_logger(
    #     console_display=True
    # )
    # log.info('아메리카노 마시고 싶다.')
    # log.error('이건 에러 문구가 나올지도 모른다.')
    # pass

if __name__ == '__main__':
    main()
    