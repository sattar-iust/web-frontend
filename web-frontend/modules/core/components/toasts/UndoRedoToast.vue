<template>
  <Alert
    simple
    shadow
    :icon="stateContent.icon"
    :loading="stateContent.loading"
    :title="stateContent.title"
  >
    {{ stateContent.content }}
  </Alert>
</template>

<script>
import { UNDO_REDO_STATES } from '@baserow/modules/core/utils/undoRedoConstants'

export default {
  name: 'UndoRedoToast',
  props: {
    state: {
      type: String,
      required: true,
    },
  },
  computed: {
    stateContent() {
      function base({ loading = false, icon = '', title = '', content = '' }) {
        return { loading, icon, title, content }
      }

      switch (this.state) {
        case UNDO_REDO_STATES.UNDONE:
          return base({
            icon: 'check',
            title: this.$t('undoRedoToast.undoneTitle'),
            content: this.$t('undoRedoToast.undoneText'),
          })
        case UNDO_REDO_STATES.REDONE:
          return base({
            icon: 'check',
            title: this.$t('undoRedoToast.redoneTitle'),
            content: this.$t('undoRedoToast.redoneText'),
          })
        case UNDO_REDO_STATES.UNDOING:
          return base({
            loading: true,
            title: this.$t('undoRedoToast.undoingTitle'),
            content: this.$t('undoRedoToast.undoingText'),
          })
        case UNDO_REDO_STATES.REDOING:
          return base({
            loading: true,
            title: this.$t('undoRedoToast.redoingTitle'),
            content: this.$t('undoRedoToast.redoingText'),
          })
        case UNDO_REDO_STATES.NO_MORE_UNDO:
          return base({
            icon: 'times',
            title: this.$t('undoRedoToast.failed'),
            content: this.$t('undoRedoToast.noMoreUndo'),
          })
        case UNDO_REDO_STATES.NO_MORE_REDO:
          return base({
            icon: 'times',
            title: this.$t('undoRedoToast.failed'),
            content: this.$t('undoRedoToast.noMoreRedo'),
          })
        case UNDO_REDO_STATES.ERROR_WITH_UNDO:
          return base({
            icon: 'exclamation',
            title: this.$t('undoRedoToast.failed'),
            content: this.$t('undoRedoToast.skippingUndoDueToError'),
          })
        case UNDO_REDO_STATES.ERROR_WITH_REDO:
          return base({
            icon: 'exclamation',
            title: this.$t('undoRedoToast.failed'),
            content: this.$t('undoRedoToast.skippingRedoDueToError'),
          })
        default:
          return base()
      }
    },
  },
}
</script>
