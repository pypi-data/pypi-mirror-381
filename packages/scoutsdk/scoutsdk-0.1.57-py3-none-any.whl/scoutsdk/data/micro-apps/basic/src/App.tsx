import { useConversationQuery, useScoutAppContext } from '@mirego/scout-chat';
import '@mirego/scout-chat/style.css';
import { useEffect } from 'react';
import useScoutTranslation from './hooks/use-scout-translation';

const App = () => {
  const { conversation_id } = useScoutAppContext();

  const { t } = useScoutTranslation();

  const conversationQuery = useConversationQuery({
    conversationId: conversation_id,
  });

  useEffect(() => {
    if (conversationQuery.data) {
      console.log('Current conversation : ', conversationQuery.data);
    }
  }, [conversationQuery.data]);

  return (
    <div>
      <span>{t('welcomeMessage')}</span>
      {conversation_id && (
        <span>{t('conversationMessage').replace('{{conversationId}}', conversation_id)}</span>
      )}
    </div>
  );
};

const WrappedApp = () => {
  const { conversation_id } = useScoutAppContext();
  return <App key={conversation_id} />;
};

export default WrappedApp;
