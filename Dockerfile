FROM ubuntu:rolling

ENV EXERCISM_TOKEN=$EXERCISM_TOKEN

WORKDIR /home/dev

COPY setup.sh /setup.sh 
COPY shell_color.txt /shell_color.txt

RUN chmod +x /setup.sh && /setup.sh

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]