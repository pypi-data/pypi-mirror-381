from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

import pytz
from sqlalchemy.exc import IntegrityError

from cortex.core.consumers.consumer import Consumer
from cortex.core.consumers.db.consumer import ConsumerORM
from cortex.core.exceptions.consumers import ConsumerDoesNotExistError, ConsumerAlreadyExistsError
from cortex.core.exceptions.environments import EnvironmentDoesNotExistError
from cortex.core.storage.store import CortexStorage
from cortex.core.types.telescope import TSModel
from cortex.core.workspaces.db.environment_service import EnvironmentCRUD


class ConsumerCRUD(TSModel):

    @staticmethod
    def get_consumer_by_email_and_environment(email: str, environment_id: UUID) -> Optional[Consumer]:
        db_session = CortexStorage().get_session()
        try:
            db_consumer = db_session.query(ConsumerORM).filter(
                ConsumerORM.email == email,
                ConsumerORM.environment_id == environment_id
            ).first()
            if db_consumer is None:
                return None
            return Consumer.model_validate(db_consumer, from_attributes=True)
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def add_consumer(consumer: Consumer) -> Consumer:
        db_session = CortexStorage().get_session()
        try:
            # Check if environment exists
            EnvironmentCRUD.get_environment(consumer.environment_id)
            
            # Check if consumer with same email exists in the environment
            existing_consumer = ConsumerCRUD.get_consumer_by_email_and_environment(
                consumer.email, 
                consumer.environment_id
            )
            if existing_consumer:
                raise ConsumerAlreadyExistsError(consumer.email, consumer.environment_id)

            while True:
                try:
                    consumer_id = uuid4()
                    db_consumer = ConsumerORM(
                        id=consumer_id,
                        environment_id=consumer.environment_id,
                        first_name=consumer.first_name,
                        last_name=consumer.last_name,
                        email=consumer.email,
                        organization=consumer.organization,
                        properties=consumer.properties,
                        created_at=datetime.now(pytz.UTC),
                        updated_at=datetime.now(pytz.UTC)
                    )
                    db_session.add(db_consumer)
                    db_session.commit()
                    db_session.refresh(db_consumer)
                    return Consumer.model_validate(db_consumer, from_attributes=True)
                except IntegrityError:
                    db_session.rollback()
                    continue
        except (EnvironmentDoesNotExistError, ConsumerAlreadyExistsError) as e:
            raise e
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_consumer(consumer_id: UUID) -> Consumer:
        db_session = CortexStorage().get_session()
        try:
            db_consumer = db_session.query(ConsumerORM).filter(
                ConsumerORM.id == consumer_id
            ).first()
            if db_consumer is None:
                raise ConsumerDoesNotExistError(consumer_id)
            
            return Consumer.model_validate(db_consumer, from_attributes=True)
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def get_consumers_by_environment(environment_id: UUID) -> List[Consumer]:
        db_session = CortexStorage().get_session()
        try:
            # Verify environment exists
            EnvironmentCRUD.get_environment(environment_id)
            
            db_consumers = db_session.query(ConsumerORM).filter(
                ConsumerORM.environment_id == environment_id
            ).all()
            
            return [Consumer.model_validate(c, from_attributes=True) for c in db_consumers]
        except Exception as e:
            raise e
        finally:
            db_session.close()

    @staticmethod
    def update_consumer(consumer: Consumer) -> Consumer:
        db_session = CortexStorage().get_session()
        try:
            # Get existing consumer
            db_consumer = db_session.query(ConsumerORM).filter(
                ConsumerORM.id == consumer.id
            ).first()
            if db_consumer is None:
                raise ConsumerDoesNotExistError(consumer.id)

            # Track if any changes were made
            changes_made = False

            # Check and update only allowed fields if they've changed
            if consumer.first_name != db_consumer.first_name:
                db_consumer.first_name = consumer.first_name
                changes_made = True

            if consumer.last_name != db_consumer.last_name:
                db_consumer.last_name = consumer.last_name
                changes_made = True

            if consumer.email != db_consumer.email:
                db_consumer.email = consumer.email
                changes_made = True

            if consumer.organization != db_consumer.organization:
                db_consumer.organization = consumer.organization
                changes_made = True

            if consumer.properties != db_consumer.properties:
                db_consumer.properties = consumer.properties
                changes_made = True

            # Only update the database if changes were made
            if changes_made:
                db_consumer.updated_at = datetime.now(pytz.UTC)
                db_session.commit()
                db_session.refresh(db_consumer)

            return Consumer.model_validate(db_consumer, from_attributes=True)
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @staticmethod
    def delete_consumer(consumer_id: UUID) -> bool:
        db_session = CortexStorage().get_session()
        try:
            result = db_session.query(ConsumerORM).filter(
                ConsumerORM.id == consumer_id
            ).delete()
            db_session.commit()
            return result > 0
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()