from django.core.management.base import BaseCommand
from app.models import User, Caregiver, Member, Address, Job, JobApplication, Appointment
from django.db import transaction
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):

        # Insert User data
        with transaction.atomic():
             # Hash the password securely
            hashed_password = make_password("12345678")
            user1 = User.objects.create(username = "user1", email='a.askarov@gmail.com', given_name='Askar', surname='Askarov', city='Astana', phone_number='+77011111111', profile_description='I am a good person', password=hashed_password)
            user2 = User.objects.create(username = "user2", email='d.dulatov@mail.ru', given_name='Dulat', surname='Dulatov', city='Almaty', phone_number='+77078855888', profile_description='Searching for help', password=hashed_password)
            user3 = User.objects.create(username = "user3", email='saden.sad@gmail.com', given_name='Saden', surname='Sadenoc', city='Astana', phone_number='+77023069807', profile_description='Is there a job for me? Ready to help', password=hashed_password)
            user4 = User.objects.create(username = "user4", email='a.bcd@list.ru', given_name='Aman', surname='Baced', city='Astana', phone_number='+77070658558', profile_description='Take care', password=hashed_password)
            user5 = User.objects.create(username = "user5", email='marat@yahoo.com', given_name='Marat', surname='Kudaibergen', city='Almaty', phone_number='+77012222222', profile_description='In need for good people', password=hashed_password)
            user6 = User.objects.create(username = "user6", email='bolatov.bolat@yahoo.com', given_name='Bolat', surname='Bolatov', city='Almaty', phone_number='+77013344566', profile_description='Just Bolatov', password=hashed_password)
            user7 = User.objects.create(username = "user7", email='asfas@mail.ru', given_name='Asan', surname='Masan', city='Astana', phone_number='+77070664558', profile_description="Didn't consider thinking of it", password=hashed_password)
            user8 = User.objects.create(username = "user8", email='madi.bcd@list.ru', given_name='Madi', surname='Madiyarov', city='Astana', phone_number='+77070668756', profile_description='Please be nice', password=hashed_password)

        # Insert Caregiver data
        with transaction.atomic():
            caregiver1 = Caregiver.objects.create(user=user1, photo=b'213141414', gender='f', caregiving_type='babysitter', hourly_rate=12.5)
            caregiver2 = Caregiver.objects.create(user=user2, photo=b'2636326236', gender='m', caregiving_type='caregiver for elderly', hourly_rate=3.2)
            caregiver3 = Caregiver.objects.create(user=user3, photo=b'75235255', gender='m', caregiving_type='playmate for children', hourly_rate=15.65)

        # Insert Member data
        with transaction.atomic():
            member1 = Member.objects.create(user=user4, house_rules='No pets allowed.')
            member2 = Member.objects.create(user=user5, house_rules='No candies for elders.')
            member3 = Member.objects.create(user=user6, house_rules='No TV, computer games and no pets.')
            member4 = Member.objects.create(user=user7, house_rules='No candies for elders.')
            member5 = Member.objects.create(user=user8, house_rules='No TV, computer games and no pets.')

        # Insert Address data
        with transaction.atomic():
            address1 = Address.objects.create(member=member1, house_number='20a', street='Turkestan street', town='Astana')
            address2 = Address.objects.create(member=member2, house_number='1', street='Abylai Khan street', town='Almaty')
            address3 = Address.objects.create(member=member3, house_number='32/2', street='Karasai Batyr street', town='Almaty')
            address4 = Address.objects.create(member=member4, house_number='13', street='Turan street', town='Astana')
            address5 = Address.objects.create(member=member5, house_number='32/1', street='Turan street', town='Astana')

        # Insert Job data
        with transaction.atomic():
            job1 = Job.objects.create(member=member1, required_caregiving_type='babysitter', other_requirements='Daily job 9:00-17:00.', date_posted='2023-12-13')
            job2 = Job.objects.create(member=member2, required_caregiving_type='caregiver for elderly', other_requirements='If you are good with pets it is great. Be gentle with him. Weekly 17:00-19:30', date_posted='2023-10-05')
            job3 = Job.objects.create(member=member3, required_caregiving_type='playmate for children', other_requirements='The whole day once a week.', date_posted='2023-09-29')
            job4 = Job.objects.create(member=member3, required_caregiving_type='babysitter', other_requirements='Weekly 12:00-14:09. I need gentle care for my baby please', date_posted='2023-11-11')
            job5 = Job.objects.create(member=member2, required_caregiving_type='caregiver for elderly', other_requirements='Please come every other day 12:30-18:30', date_posted='2023-10-09')
            job6 = Job.objects.create(member=member1, required_caregiving_type='playmate for children', other_requirements='Every day 11:00-19:45', date_posted='2023-09-27')
            job7 = Job.objects.create(member=member1, required_caregiving_type='caregiver for elderly', other_requirements='Anytime', date_posted='2023-03-09')
            job8 = Job.objects.create(member=member3, required_caregiving_type='playmate for children', other_requirements='Every day whole day', date_posted='2023-02-27')

        # Insert JobApplication data
        with transaction.atomic():
            ja1 = JobApplication.objects.create(job=job1, caregiver=caregiver2, date_applied='2023-10-06')
            ja2 = JobApplication.objects.create(job=job2, caregiver=caregiver2, date_applied='2023-10-08')
            ja3 = JobApplication.objects.create(job=job1, caregiver=caregiver3, date_applied='2023-10-01')
            ja4 = JobApplication.objects.create(job=job3, caregiver=caregiver2, date_applied='2023-10-15')
            ja5 = JobApplication.objects.create(job=job2, caregiver=caregiver3, date_applied='2023-09-28')

        # Insert Appointment data
        with transaction.atomic():
            app1 = Appointment.objects.create(
                caregiver=caregiver2,
                member=member2,
                appointment_date='2023-10-10',
                appointment_time='16:30:00',
                work_hours=5.4,
                status='Accepted'
            )
            app2 = Appointment.objects.create(
                caregiver=caregiver2,
                member=member1,
                appointment_date='2023-10-15',
                appointment_time='12:00:00',
                work_hours=12,
                status='Accepted'
            )
            app3 = Appointment.objects.create(
                caregiver=caregiver1,
                member=member2,
                appointment_date='2023-10-07',
                appointment_time='16:00:00',
                work_hours=3,
                status='Declined'
            )
            app4 = Appointment.objects.create(
                caregiver=caregiver1,
                member=member3,
                appointment_date='2023-10-17',
                appointment_time='10:30:00',
                work_hours=4.2,
                status='Accepted'
            )


        self.stdout.write(self.style.SUCCESS('Data population completed successfully.'))
